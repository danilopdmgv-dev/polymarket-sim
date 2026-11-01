# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-11-01 01:20 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1320.20 (-34.0%) | **Cash:** $1202.44 | **Abertas:** 7 | **Ciclos:** 56
**Fechadas:** 93 | **Win rate:** 31% | **PnL realizado:** $-675.17
**Chamadas ao LLM hoje:** 9

## Por motivo de saida
- resolvido: 1 trades, PnL $-46.54
- stop-loss: 63 trades, PnL $-1154.22
- take-profit: 29 trades, PnL $+525.59

## Por categoria
- Clima: 82 trades, win 29%, PnL $-720.13
- Outros: 2 trades, win 50%, PnL $+4.14
- Politica: 9 trades, win 44%, PnL $+40.81
- **Clima INVERSO (compra o lado oposto ao modelo):** 33 trades, win 48%, PnL $-3.61

## Calibracao do LLM vs mercado (302 mercados resolvidos)
- Brier LLM: 0.2982 | Brier mercado: 0.2159 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (223): LLM 0.3436 vs mercado 0.2303
  - Economia/Dados (6): LLM 0.0559 vs mercado 0.0628
  - Entretenimento (17): LLM 0.1604 vs mercado 0.1664
  - Outros (25): LLM 0.1393 vs mercado 0.1359
  - Politica (31): LLM 0.2217 vs mercado 0.2335
- Fonte clima (223): modelo 0.3436 vs mercado 0.2303 -> PERDENDO
- Fonte llm (79): modelo 0.1699 vs mercado 0.1752 -> GANHANDO
- Clima (204): sigma largo 0.3517 | sigma estreito 0.3262 | mercado 0.2319

## Posicoes abertas
- YES Will Аndrey Gyurov win the next Bulgarian presidential elect | entrada 0.35, agora 0.32, LLM 0.52, edge 0.08, medium | Market underprices Gyurov's chances given broad establishment endorsements from former PMs and presi
- YES Will the highest temperature in Paris be 13°C on November 1? | entrada 0.44, agora 0.39, LLM 0.18, edge 0.11, medium | Modelo 0.18 vs mercado 0.41
- YES Will the highest temperature in Karachi be 36°C on November  | entrada 0.51, agora 0.47, LLM 0.17, edge 0.14, medium | Modelo 0.17 vs mercado 0.47
- YES Will the highest temperature in Houston be between 84-85°F o | entrada 0.51, agora 0.52, LLM 0.20, edge 0.14, medium | Modelo 0.20 vs mercado 0.48
- YES Will the highest temperature in Moscow be 10°C on November 1 | entrada 0.45, agora 0.49, LLM 0.17, edge 0.14, medium | Modelo 0.17 vs mercado 0.43
- YES Will the highest temperature in Jeddah be 35°C on November 1 | entrada 0.48, agora 0.42, LLM 0.16, edge 0.16, medium | Modelo 0.16 vs mercado 0.46
- YES Will the highest temperature in Tokyo be 20°C on November 1? | entrada 0.52, agora 0.57, LLM 0.25, edge 0.11, medium | Modelo 0.25 vs mercado 0.49

## Ultimas 10 fechadas
- YES Will voter turnout in the second round of the 2026 | stop-loss | $-8.24 | 17.3h
- YES Will the highest temperature in Hong Kong be 28°C  | stop-loss | $-5.02 | 7.8h
- YES Will the highest temperature in Tel Aviv be 27°C o | take-profit | $+2.68 | 10.7h
- YES Will the highest temperature in Buenos Aires be 26 | take-profit | $+17.29 | 19.9h
- YES Will the highest temperature in Cape Town be 21°C  | take-profit | $+3.48 | 6.3h
- YES Will the highest temperature in Madrid be 22°C on  | stop-loss | $-5.21 | 6.3h
- YES Will the highest temperature in Paris be 15°C on O | take-profit | $+5.49 | 12.3h
- YES Will the highest temperature in Milan be 17°C on O | take-profit | $+6.28 | 12.3h
- YES Will the highest temperature in Singapore be 33°C  | take-profit | $+13.97 | 18.2h
- YES Will the highest temperature in Tokyo be 23°C on O | take-profit | $+14.45 | 18.2h
