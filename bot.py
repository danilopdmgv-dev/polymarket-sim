"""
Polymarket Survival Sim - 1 ciclo por execucao (GitHub Actions). SO SIMULACAO.
Estado em state.json, relatorio em report.md.
Env (Secrets): LLM_API_KEY, LLM_BASE_URL, LLM_MODEL
"""
import os, re, json, time, urllib.parse, datetime as dt
import requests, feedparser
from openai import OpenAI

VERSION = "v3-alto-volume"
START_CASH = 50.0
KILL_FLOOR = 25.0

# Entrada
LLM_PER_CYCLE = 8
MAX_REEVAL = 8
LLM_CACHE_MIN = 20
MIN_LIQ, MIN_VOL = 5000, 1500
MAX_SPREAD = 0.05
PRICE_MIN, PRICE_MAX = 0.08, 0.92
DAYS_MIN, DAYS_MAX = 0.1, 2.0
SHRINK = 0.5
MIN_EDGE = 0.05
KELLY_FRAC = 0.25
POS_PCT = {"medium": 0.03, "high": 0.04}
MIN_ORDER = 1.0
MAX_OPEN = 25
MAX_PER_CAT = 6

# Saida
TP_CAPTURE = 0.75
STOP_LOSS = 0.30
MAX_HOLD_DAYS = 2.5
BREAK_MIN_HOURS = 2
BREAK_GAP = 0.05
BREAK_MARGIN = 0.02
BREAK_CONFIRM = 2

GAMMA = "https://gamma-api.polymarket.com"
STATE, LOG, REPORT = "state.json", "trades.log", "report.md"
T0 = time.time()
LLM_DOWN = False            # vira True se o LLM der 429/503 (limite ou instabilidade)
DAILY_LLM_BUDGET = 400      # teto de consultas por dia
SKIP_CATS = {"Esportes"}    # categorias que NAO vao ao LLM (deixe vazio {} para incluir)

llm = OpenAI(api_key=os.getenv("LLM_API_KEY") or "missing",
             base_url=os.getenv("LLM_BASE_URL") or "https://api.openai.com/v1",
             timeout=30, max_retries=1)
MODEL = os.getenv("LLM_MODEL") or "gpt-4o-mini"

CATS = [
    ("Cripto", r"bitcoin|\bbtc\b|ethereum|\beth\b|solana|\bxrp\b|crypto|dogecoin"),
    ("Esportes", r"\bvs\.?\b|\bnba\b|\bnfl\b|\bmlb\b|\bnhl\b|\bufc\b|premier league|champions league|ballon|spread:|o/u"),
    ("Politica", r"election|senate|house|president|congress|governor|trump|vote|minister|parliament|ceasefire|tariff"),
    ("Economia/Dados", r"\bfed\b|interest rate|inflation|\bcpi\b|\bgdp\b|jobs report|unemployment|earnings|s&p|nasdaq|oil"),
    ("Clima", r"temperature|hurricane|rain|snow|weather"),
    ("Entretenimento", r"oscar|grammy|movie|box office|album|song|tweet|netflix|emmy|billboard"),
]


# ---------------- UTIL ----------------
def now():
    return time.time()


def log(msg):
    line = f"{dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M:%S}Z {msg}"
    print(line)
    with open(LOG, "a") as f:
        f.write(line + "\n")


def fnum(x, d=0.0):
    try:
        return float(x)
    except (TypeError, ValueError):
        return d


def jl(x):
    return json.loads(x) if isinstance(x, str) else (x or [])


def parse_ts(v):
    if not v:
        return None
    try:
        v = str(v).replace("Z", "+00:00").replace(" ", "T")
        if re.search(r"[+-]\d\d$", v):
            v += ":00"
        d = dt.datetime.fromisoformat(v)
        if d.tzinfo is None:
            d = d.replace(tzinfo=dt.timezone.utc)
        return d.timestamp()
    except Exception:
        return None


def load():
    if os.path.exists(STATE):
        return json.load(open(STATE))
    return {"cash": START_CASH, "positions": [], "closed": [], "cache": {},
            "estimates": {}, "history": [], "llm_calls": {}, "killed": False, "cycles": 0}


def save(s):
    json.dump(s, open(STATE, "w"), indent=1)


def slippage(liq):
    return 0.010 if liq >= 20000 else (0.015 if liq >= 10000 else 0.025)


def category(q):
    for name, rx in CATS:
        if re.search(rx, q, re.I):
            return name
    return "Outros"


# ---------------- DADOS ----------------
def fetch_markets():
    out, off = [], 0
    t0 = dt.datetime.now(dt.timezone.utc)
    params = {"active": "true", "closed": "false", "limit": 100,
              "order": "volume24hr", "ascending": "false",
              "end_date_min": (t0 + dt.timedelta(days=DAYS_MIN)).isoformat(),
              "end_date_max": (t0 + dt.timedelta(days=DAYS_MAX)).isoformat()}
    while off < 3000:
        r = requests.get(f"{GAMMA}/markets", params={**params, "offset": off}, timeout=30)
        r.raise_for_status()
        batch = r.json()
        if not batch:
            break
        out += batch
        off += 100
        if fnum(batch[-1].get("volume24hr")) < MIN_VOL:
            break
    return out


def fetch_market(mid):
    r = requests.get(f"{GAMMA}/markets/{mid}", timeout=30)
    r.raise_for_status()
    return r.json()


def parse(m):
    try:
        prices = [float(p) for p in jl(m.get("outcomePrices"))]
        tokens = jl(m.get("clobTokenIds"))
        end = parse_ts(m.get("endDate"))
        bid, ask = fnum(m.get("bestBid")), fnum(m.get("bestAsk"))
        if len(prices) != 2 or len(tokens) != 2 or end is None or not (0 < ask <= 1):
            return None
        q = m["question"]
        return dict(id=str(m["id"]), q=q, desc=(m.get("description") or "")[:600],
                    yes=prices[0], bid=bid, ask=ask, tokens=tokens, end=end,
                    days=(end - now()) / 86400,
                    liq=fnum(m.get("liquidityNum") or m.get("liquidity")),
                    vol=fnum(m.get("volume24hr")), cat=category(q),
                    start=parse_ts(m.get("gameStartTime")))
    except Exception:
        return None


def resolution(raw):
    """Retorna 'YES', 'NO', 'VOID' ou None se ainda nao resolvido."""
    try:
        if not raw.get("closed"):
            return None
        pr = [float(p) for p in jl(raw.get("outcomePrices"))]
        if len(pr) == 2:
            if pr[0] >= 0.99:
                return "YES"
            if pr[1] >= 0.99:
                return "NO"
        return "VOID"
    except Exception:
        return None


def discard_reason(m):
    q = m["q"]
    if re.search(r"balance of power|\bboth\b|&|\bparlay\b|\bcombo\b", q, re.I):
        return "combinado"
    if m["cat"] == "Cripto":
        return "cripto"
    if re.search(r"\bvs\.?\b|spread:|o/u", q, re.I) and m["start"] and m["start"] - now() < 3 * 3600:
        return "esporte_vivo"
    return None


def base_ok(m):
    return (m["liq"] >= MIN_LIQ and m["vol"] >= MIN_VOL
            and PRICE_MIN <= m["yes"] <= PRICE_MAX
            and DAYS_MIN <= m["days"] <= DAYS_MAX
            and (m["ask"] - m["bid"]) <= MAX_SPREAD)


def news(q, n=6):
    url = "https://news.google.com/rss/search?q=" + urllib.parse.quote(q) + "&hl=en-US"
    try:
        f = feedparser.parse(requests.get(url, timeout=15).content)
        return [f"- {e.title} ({e.get('published', '')})" for e in f.entries[:n]]
    except Exception:
        return []


# ---------------- LLM ----------------
def ask_llm(m):
    global LLM_DOWN
    if LLM_DOWN:
        raise RuntimeError("LLM indisponivel neste ciclo")
    heads = "\n".join(news(m["q"])) or "(sem noticias encontradas)"
    today = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    prompt = f"""Voce e um superforecaster calibrado e CETICO. Estime a probabilidade de SIM.
Agora: {today}
Mercado: {m['q']}
Regras: {m['desc']}
Preco atual do mercado (SIM): {m['yes']:.3f}
Dias ate resolver: {m['days']:.2f}
Noticias recentes:
{heads}

Considere dados oficiais agendados, resultados parciais, escalacoes, previsoes meteorologicas e comunicados recentes.
Se o preco do mercado ja reflete o consenso publico, responda com p igual ao preco e confidence="low".
So se afaste do preco se a evidencia trouxer informacao NOVA que o mercado provavelmente ainda nao incorporou.
Descrever o favorito ou o consenso NAO e evidencia de erro de preco.
Responda SOMENTE JSON:
{{"p": 0-1, "confidence": "low|medium|high", "evidence": ["1 a 3 fatos concretos e recentes com numero ou data"], "market_misprice_reason": "uma frase: por que o mercado esta errado", "reason": "uma frase"}}"""
    try:
        r = llm.chat.completions.create(model=MODEL, temperature=0,
                                        messages=[{"role": "user", "content": prompt}])
    except Exception as e:
        if any(k in str(e) for k in ("429", "RESOURCE_EXHAUSTED", "503", "UNAVAILABLE", "quota")):
            LLM_DOWN = True
            log("LLM com limite/instabilidade: pulando as consultas restantes deste ciclo.")
        raise
    txt = r.choices[0].message.content or ""
    d = json.loads(txt[txt.find("{"): txt.rfind("}") + 1])
    p = min(max(float(d["p"]), 0.01), 0.99)
    conf = str(d.get("confidence", "low")).lower()
    if conf not in ("low", "medium", "high"):
        conf = "low"
    ev = d.get("evidence") or []
    ev = [ev] if isinstance(ev, str) else ev
    ev = [str(e) for e in ev][:3]
    why = str(d.get("market_misprice_reason") or "").strip()
    if not (ev and any(re.search(r"\d", e) for e in ev) and why):
        conf = "low"
    return dict(p=p, conf=conf, evidence=ev, misprice=why, reason=str(d.get("reason", ""))[:200])


def get_estimate(s, m, force=False):
    global LLM_DOWN
    c = s["cache"].get(m["id"])
    if c and not force and now() - c["t"] < LLM_CACHE_MIN * 60 and abs(c["yes"] - m["yes"]) < 0.03:
        return c["est"], False
    day = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")
    if s["llm_calls"].get(day, 0) >= DAILY_LLM_BUDGET:
        LLM_DOWN = True
        raise RuntimeError("orcamento diario de consultas atingido")
    time.sleep(4.5)  # respeita ~15 consultas/minuto do plano gratuito
    est = ask_llm(m)
    s["llm_calls"][day] = s["llm_calls"].get(day, 0) + 1
    s["cache"][m["id"]] = dict(t=now(), yes=m["yes"], est=est)
    if m["id"] not in s["estimates"]:  # guarda a 1a estimativa (sem look-ahead)
        s["estimates"][m["id"]] = dict(q=m["q"], p=est["p"], yes=m["yes"], conf=est["conf"],
                                       cat=m["cat"], end=m["end"], t=now(), resolved=None,
                                       version=VERSION)
    return est, True


# ---------------- CARTEIRA ----------------
def equity(s):
    return s["cash"] + sum(p["shares"] * p.get("mark", p["entry"]) for p in s["positions"])


def sell_price(m, side, liq):
    sl = slippage(liq)
    px = m["bid"] if side == "YES" else 1 - m["ask"]
    return max(0.01, px - sl)


def close_pos(s, pos, price, reason, extra=None):
    proceeds = pos["shares"] * price
    s["cash"] += proceeds
    rec = {**pos, "exit": price, "reason": reason, "pnl": proceeds - pos["cost"],
           "closed_t": now(), "held_h": (now() - pos["t"]) / 3600, **(extra or {})}
    s["closed"].append(rec)
    log(f"SELL {pos['side']} [{reason}] {pos['q'][:50]} @ {price:.3f} pnl=${rec['pnl']:+.2f}")


def kelly_size(p, price, eq, conf):
    f = max(0.0, (p - price) / (1 - price)) * KELLY_FRAC
    return min(f, POS_PCT.get(conf, 0)) * eq


# ---------------- RESOLUCAO ----------------
def check_resolutions(s):
    pend = [(mid, e) for mid, e in s["estimates"].items()
            if e["resolved"] is None and e["end"] < now()]
    pend.sort(key=lambda x: x[1]["end"])
    for mid, e in pend[:30]:
        try:
            res = resolution(fetch_market(mid))
            if res:
                e["resolved"] = res
        except Exception as ex:
            log(f"erro resolucao {mid}: {ex}")


# ---------------- SAIDAS ----------------
def manage_exits(s, st):
    keep, reevals = [], 0
    for pos in s["positions"]:
        try:
            raw = fetch_market(pos["mid"])
            res = resolution(raw)
            if res:
                if pos["mid"] in s["estimates"]:
                    s["estimates"][pos["mid"]]["resolved"] = res
                win = (res == pos["side"])
                price = 1.0 if win else (0.0 if res in ("YES", "NO") else pos["entry"])
                close_pos(s, pos, price, "resolvido" if res != "VOID" else "anulado")
                st["sells"] += 1
                continue
            m = parse(raw)
            if not m:
                keep.append(pos)
                continue
            px = sell_price(m, pos["side"], m["liq"])
            pos["mark"] = m["bid"] if pos["side"] == "YES" else 1 - m["ask"]
            held_h = (now() - pos["t"]) / 3600
            target = pos["entry"] + TP_CAPTURE * (pos["fair"] - pos["entry"])
            reason = None
            if px >= target:
                reason = "take-profit"
            elif px <= pos["entry"] * (1 - STOP_LOSS):
                reason = "stop-loss"
            elif held_h / 24 >= MAX_HOLD_DAYS:
                reason = "tempo-maximo"
            elif held_h >= BREAK_MIN_HOURS and reevals < MAX_REEVAL and not LLM_DOWN:
                est, called = get_estimate(s, m)
                reevals += 1 if called else 0
                p_new = est["p"] if pos["side"] == "YES" else 1 - est["p"]
                cond = (est["conf"] in ("medium", "high")
                        and p_new <= pos["entry"] - BREAK_GAP
                        and px >= p_new + BREAK_MARGIN)
                pos["breakCount"] = pos.get("breakCount", 0) + 1 if cond else 0
                if pos["breakCount"] >= BREAK_CONFIRM:
                    close_pos(s, pos, px, "tese-quebrada",
                              dict(p_new=p_new, new_reason=est["reason"], new_evidence=est["evidence"]))
                    st["sells"] += 1
                    continue
            if reason:
                close_pos(s, pos, px, reason)
                st["sells"] += 1
            else:
                keep.append(pos)
        except Exception as e:
            log(f"erro saida {pos['q'][:40]}: {e}")
            keep.append(pos)
    s["positions"] = keep


# ---------------- ENTRADAS ----------------
def find_entries(s, st):
    held = {p["mid"] for p in s["positions"]}
    raw = [parse(m) for m in fetch_markets()]
    st["scanned"] = len(raw)
    cands = []
    for m in raw:
        if not m or m["id"] in held or not base_ok(m):
            continue
        why = discard_reason(m)
        if not why and m["cat"] in SKIP_CATS:
            why = "categoria_" + m["cat"]
        if why:
            st["filtered"][why] = st["filtered"].get(why, 0) + 1
            continue
        cands.append(m)
    st["passed"] = len(cands)
    cands.sort(key=lambda m: (-m["vol"], m["ask"] - m["bid"]))

    calls = 0
    for m in cands:
        if calls >= LLM_PER_CYCLE or len(s["positions"]) >= MAX_OPEN or time.time() - T0 > 300:
            break
        if sum(1 for p in s["positions"] if p["cat"] == m["cat"]) >= MAX_PER_CAT:
            continue
        try:
            est, called = get_estimate(s, m)
        except Exception as e:
            log(f"erro LLM {m['q'][:40]}: {str(e)[:150]}")
            calls += 1
            if LLM_DOWN:
                break
            continue
        calls += 1 if called else 0
        if est["conf"] == "low":
            continue
        p_adj = m["yes"] + SHRINK * (est["p"] - m["yes"])
        sl = slippage(m["liq"])
        if p_adj >= m["yes"]:
            side, price, p_side = "YES", min(0.99, m["ask"] + sl), p_adj
        else:
            side, price, p_side = "NO", min(0.99, 1 - m["bid"] + sl), 1 - p_adj
        edge = p_side - price
        if edge < MIN_EDGE:
            continue
        usd = min(kelly_size(p_side, price, equity(s), est["conf"]), s["cash"])
        if usd < MIN_ORDER:
            continue
        s["cash"] -= usd
        s["positions"].append(dict(
            mid=m["id"], q=m["q"], cat=m["cat"], side=side,
            token=m["tokens"][0 if side == "YES" else 1], entry=price, fair=p_side,
            shares=usd / price, cost=usd, t=now(), mark=price, conf=est["conf"],
            llm_p=est["p"], mkt_yes=m["yes"], edge=edge, evidence=est["evidence"],
            misprice=est["misprice"], version=VERSION))
        st["buys"] += 1
        log(f"BUY {side} {m['q'][:50]} @ {price:.3f} ${usd:.2f} edge={edge:.3f} "
            f"conf={est['conf']} | {est['misprice']}")
    st["llm"] = calls


# ---------------- RELATORIO ----------------
def report(s):
    eq = equity(s)
    cl = s["closed"]
    wins = [c for c in cl if c["pnl"] > 0]
    day = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")
    L = [f"# Polymarket Survival Sim ({VERSION})",
         f"_Atualizado {dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC. SIMULACAO, sem dinheiro real._", "",
         f"**Equity:** ${eq:.2f} ({(eq / START_CASH - 1) * 100:+.1f}%) | **Cash:** ${s['cash']:.2f} | "
         f"**Abertas:** {len(s['positions'])} | **Ciclos:** {s['cycles']}"
         + (" | **KILL SWITCH ATIVO**" if s["killed"] else ""),
         f"**Fechadas:** {len(cl)} | **Win rate:** "
         f"{(len(wins) / len(cl) * 100 if cl else 0):.0f}% | **PnL realizado:** "
         f"${sum(c['pnl'] for c in cl):+.2f}",
         f"**Chamadas ao LLM hoje:** {s['llm_calls'].get(day, 0)}", "", "## Por motivo de saida"]
    for k in sorted({c["reason"] for c in cl}):
        g = [c for c in cl if c["reason"] == k]
        L.append(f"- {k}: {len(g)} trades, PnL ${sum(c['pnl'] for c in g):+.2f}")
    L += ["", "## Por categoria"]
    for k in sorted({c["cat"] for c in cl}):
        g = [c for c in cl if c["cat"] == k]
        w = sum(1 for c in g if c["pnl"] > 0)
        L.append(f"- {k}: {len(g)} trades, win {w / len(g) * 100:.0f}%, PnL ${sum(c['pnl'] for c in g):+.2f}")
    res = [e for e in s["estimates"].values() if e["resolved"] in ("YES", "NO")]
    L += ["", f"## Calibracao do LLM vs mercado ({len(res)} mercados resolvidos)"]
    if res:
        def brier(key):
            return sum((e[key] - (1 if e["resolved"] == "YES" else 0)) ** 2 for e in res) / len(res)
        bl, bm = brier("p"), brier("yes")
        L.append(f"- Brier LLM: {bl:.4f} | Brier mercado: {bm:.4f} (menor e melhor)")
        L.append("- **LLM esta " + ("GANHANDO" if bl < bm else "PERDENDO") + " do mercado.**")
        for k in sorted({e["cat"] for e in res}):
            g = [e for e in res if e["cat"] == k]
            bl_k = sum((e["p"] - (e["resolved"] == "YES")) ** 2 for e in g) / len(g)
            bm_k = sum((e["yes"] - (e["resolved"] == "YES")) ** 2 for e in g) / len(g)
            L.append(f"  - {k} ({len(g)}): LLM {bl_k:.4f} vs mercado {bm_k:.4f}")
    if len(res) < 30:
        L.append(f"- Amostra pequena: conclusoes so com 30+ resolvidos (faltam {30 - len(res)}).")
    L += ["", "## Posicoes abertas"]
    for p in s["positions"]:
        L.append(f"- {p['side']} {p['q'][:60]} | entrada {p['entry']:.2f}, agora {p.get('mark', p['entry']):.2f}, "
                 f"LLM {p['llm_p']:.2f}, edge {p['edge']:.2f}, {p['conf']} | {p['misprice'][:100]}")
    L += ["", "## Ultimas 10 fechadas"]
    for c in cl[-10:][::-1]:
        L.append(f"- {c['side']} {c['q'][:50]} | {c['reason']} | ${c['pnl']:+.2f} | {c['held_h']:.1f}h")
    open(REPORT, "w").write("\n".join(L) + "\n")


# ---------------- MAIN ----------------
def main():
    if os.path.exists(LOG) and os.path.getsize(LOG) > 200_000:
        lines = open(LOG).read().splitlines()[-1000:]
        open(LOG, "w").write("\n".join(lines) + "\n")
    s = load()
    s["cycles"] += 1
    st = dict(scanned=0, passed=0, llm=0, buys=0, sells=0, filtered={})
    try:
        check_resolutions(s)
        manage_exits(s, st)
        eq = equity(s)
        if eq < KILL_FLOOR and not s["killed"]:
            s["killed"] = True
            log(f"KILL SWITCH: equity ${eq:.2f} < ${KILL_FLOOR}")
        if not s["killed"]:
            find_entries(s, st)
    except Exception as e:
        log(f"erro no ciclo: {e}")
    s["history"].append(dict(t=now(), equity=round(equity(s), 2)))
    s["history"] = s["history"][-2000:]
    s["cache"] = {k: v for k, v in s["cache"].items() if now() - v["t"] < 6 * 3600}
    log(f"ciclo {s['cycles']}: lidos={st['scanned']} filtro={st['passed']} llm={st['llm']} "
        f"compras={st['buys']} vendas={st['sells']} descartados={st['filtered']} "
        f"equity=${equity(s):.2f}")
    report(s)
    save(s)


if __name__ == "__main__":
    main()
