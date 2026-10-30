# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-10-30 22:47 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1289.14 (-35.5%) | **Cash:** $1212.17 | **Abertas:** 6 | **Ciclos:** 50
**Fechadas:** 80 | **Win rate:** 26% | **PnL realizado:** $-708.59
**Chamadas ao LLM hoje:** 35

## Por motivo de saida
- resolvido: 1 trades, PnL $-46.54
- stop-loss: 58 trades, PnL $-1119.35
- take-profit: 21 trades, PnL $+457.30

## Por categoria
- Clima: 70 trades, win 23%, PnL $-761.78
- Outros: 2 trades, win 50%, PnL $+4.14
- Politica: 8 trades, win 50%, PnL $+49.05
- **Clima INVERSO (compra o lado oposto ao modelo):** 21 trades, win 38%, PnL $-45.27

## Calibracao do LLM vs mercado (248 mercados resolvidos)
- Brier LLM: 0.2971 | Brier mercado: 0.2157 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (188): LLM 0.3375 vs mercado 0.2286
  - Economia/Dados (6): LLM 0.0559 vs mercado 0.0628
  - Entretenimento (12): LLM 0.2079 vs mercado 0.2153
  - Outros (21): LLM 0.1351 vs mercado 0.1292
  - Politica (21): LLM 0.2169 vs mercado 0.2313
- Fonte clima (188): modelo 0.3375 vs mercado 0.2286 -> PERDENDO
- Fonte llm (60): modelo 0.1704 vs mercado 0.1755 -> GANHANDO
- Clima (169): sigma largo 0.3466 | sigma estreito 0.3204 | mercado 0.2304

## Posicoes abertas
- YES Will the highest temperature in Shenzhen be 30°C on October  | entrada 0.62, agora 0.62, LLM 0.20, edge 0.21, medium | Modelo 0.20 vs mercado 0.59
- YES Will the highest temperature in Wellington be 14°C on Octobe | entrada 0.53, agora 0.51, LLM 0.21, edge 0.16, medium | Modelo 0.21 vs mercado 0.51
- YES Will the highest temperature in Tokyo be 23°C on October 31? | entrada 0.45, agora 0.47, LLM 0.22, edge 0.10, medium | Modelo 0.22 vs mercado 0.42
- YES Will the highest temperature in Singapore be 33°C on October | entrada 0.47, agora 0.47, LLM 0.14, edge 0.15, medium | Modelo 0.14 vs mercado 0.44
- YES Will the highest temperature in Tel Aviv be 27°C on October  | entrada 0.41, agora 0.33, LLM 0.20, edge 0.08, medium | Modelo 0.20 vs mercado 0.38
- YES Will the highest temperature in Buenos Aires be 26°C on Octo | entrada 0.40, agora 0.40, LLM 0.05, edge 0.14, medium | Modelo 0.05 vs mercado 0.35

## Ultimas 10 fechadas
- YES Will the highest temperature in Houston be between | take-profit | $+13.53 | 22.2h
- YES Will Vivek Ramaswamy pull the Amy Acton mother ad? | take-profit | $+22.65 | 12.2h
- YES Will the highest temperature in Istanbul be 15°C o | take-profit | $+5.98 | 22.2h
- YES Will the highest temperature in Paris be 15°C on O | stop-loss | $-12.86 | 13.2h
- YES Will the highest temperature in Amsterdam be 13°C  | take-profit | $+11.30 | 13.2h
- YES Will the highest temperature in Tel Aviv be 25°C o | take-profit | $+6.06 | 17.0h
- YES Will the highest temperature in Los Angeles be bet | stop-loss | $-5.32 | 22.0h
- YES Will the highest temperature in Beijing be 22°C on | stop-loss | $-8.43 | 3.7h
- YES Will the highest temperature in Amsterdam be 14°C  | stop-loss | $-5.85 | 8.2h
- YES Will the highest temperature in Shanghai be 24°C o | stop-loss | $-8.17 | 30.1h
