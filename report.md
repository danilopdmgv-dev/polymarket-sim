# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-10-31 07:58 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1312.61 (-34.4%) | **Cash:** $1159.96 | **Abertas:** 8 | **Ciclos:** 52
**Fechadas:** 85 | **Win rate:** 28% | **PnL realizado:** $-691.92
**Chamadas ao LLM hoje:** 12

## Por motivo de saida
- resolvido: 1 trades, PnL $-46.54
- stop-loss: 60 trades, PnL $-1135.76
- take-profit: 24 trades, PnL $+490.37

## Por categoria
- Clima: 75 trades, win 25%, PnL $-745.12
- Outros: 2 trades, win 50%, PnL $+4.14
- Politica: 8 trades, win 50%, PnL $+49.05
- **Clima INVERSO (compra o lado oposto ao modelo):** 26 trades, win 42%, PnL $-28.60

## Calibracao do LLM vs mercado (260 mercados resolvidos)
- Brier LLM: 0.3004 | Brier mercado: 0.2170 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (200): LLM 0.3395 vs mercado 0.2294
  - Economia/Dados (6): LLM 0.0559 vs mercado 0.0628
  - Entretenimento (12): LLM 0.2079 vs mercado 0.2153
  - Outros (21): LLM 0.1351 vs mercado 0.1292
  - Politica (21): LLM 0.2169 vs mercado 0.2313
- Fonte clima (200): modelo 0.3395 vs mercado 0.2294 -> PERDENDO
- Fonte llm (60): modelo 0.1704 vs mercado 0.1755 -> GANHANDO
- Clima (181): sigma largo 0.3481 | sigma estreito 0.3239 | mercado 0.2312

## Posicoes abertas
- YES Will the highest temperature in Buenos Aires be 26°C on Octo | entrada 0.40, agora 0.50, LLM 0.05, edge 0.14, medium | Modelo 0.05 vs mercado 0.35
- YES Will the highest temperature in Milan be 17°C on October 31? | entrada 0.58, agora 0.64, LLM 0.29, edge 0.12, medium | Modelo 0.29 vs mercado 0.54
- YES Will the highest temperature in Paris be 15°C on October 31? | entrada 0.55, agora 0.53, LLM 0.24, edge 0.16, medium | Modelo 0.24 vs mercado 0.54
- YES Will the highest temperature in Madrid be 22°C on October 31 | entrada 0.57, agora 0.57, LLM 0.16, edge 0.19, medium | Modelo 0.16 vs mercado 0.54
- YES Will the highest temperature in Cape Town be 21°C on Novembe | entrada 0.41, agora 0.41, LLM 0.21, edge 0.09, medium | Modelo 0.21 vs mercado 0.40
- YES Will the highest temperature in Tel Aviv be 27°C on November | entrada 0.51, agora 0.51, LLM 0.20, edge 0.13, medium | Modelo 0.20 vs mercado 0.47
- YES Will Аndrey Gyurov win the next Bulgarian presidential elect | entrada 0.35, agora 0.35, LLM 0.52, edge 0.08, medium | Market underprices Gyurov's chances given broad establishment endorsements from former PMs and presi
- YES Will voter turnout in the second round of the 2026 Bulgaria  | entrada 0.19, agora 0.19, LLM 0.35, edge 0.07, medium | The market underestimates the compounding effect of voter apathy and fatigue from consecutive rounds

## Ultimas 10 fechadas
- YES Will the highest temperature in Singapore be 33°C  | take-profit | $+13.97 | 18.2h
- YES Will the highest temperature in Tokyo be 23°C on O | take-profit | $+14.45 | 18.2h
- YES Will the highest temperature in Shenzhen be 30°C o | take-profit | $+4.66 | 18.2h
- YES Will the highest temperature in Tel Aviv be 27°C o | stop-loss | $-5.62 | 7.0h
- YES Will the highest temperature in Wellington be 14°C | stop-loss | $-10.79 | 12.2h
- YES Will the highest temperature in Houston be between | take-profit | $+13.53 | 22.2h
- YES Will Vivek Ramaswamy pull the Amy Acton mother ad? | take-profit | $+22.65 | 12.2h
- YES Will the highest temperature in Istanbul be 15°C o | take-profit | $+5.98 | 22.2h
- YES Will the highest temperature in Paris be 15°C on O | stop-loss | $-12.86 | 13.2h
- YES Will the highest temperature in Amsterdam be 13°C  | take-profit | $+11.30 | 13.2h
