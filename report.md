# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-10-31 14:19 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1315.45 (-34.2%) | **Cash:** $1169.08 | **Abertas:** 8 | **Ciclos:** 53
**Fechadas:** 89 | **Win rate:** 30% | **PnL realizado:** $-681.88
**Chamadas ao LLM hoje:** 22

## Por motivo de saida
- resolvido: 1 trades, PnL $-46.54
- stop-loss: 61 trades, PnL $-1140.97
- take-profit: 27 trades, PnL $+505.62

## Por categoria
- Clima: 79 trades, win 28%, PnL $-735.08
- Outros: 2 trades, win 50%, PnL $+4.14
- Politica: 8 trades, win 50%, PnL $+49.05
- **Clima INVERSO (compra o lado oposto ao modelo):** 30 trades, win 47%, PnL $-18.56

## Calibracao do LLM vs mercado (268 mercados resolvidos)
- Brier LLM: 0.3014 | Brier mercado: 0.2164 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (208): LLM 0.3392 vs mercado 0.2281
  - Economia/Dados (6): LLM 0.0559 vs mercado 0.0628
  - Entretenimento (12): LLM 0.2079 vs mercado 0.2153
  - Outros (21): LLM 0.1351 vs mercado 0.1292
  - Politica (21): LLM 0.2169 vs mercado 0.2313
- Fonte clima (208): modelo 0.3392 vs mercado 0.2281 -> PERDENDO
- Fonte llm (60): modelo 0.1704 vs mercado 0.1755 -> GANHANDO
- Clima (189): sigma largo 0.3474 | sigma estreito 0.3228 | mercado 0.2297

## Posicoes abertas
- YES Will the highest temperature in Buenos Aires be 26°C on Octo | entrada 0.40, agora 0.43, LLM 0.05, edge 0.14, medium | Modelo 0.05 vs mercado 0.35
- YES Will the highest temperature in Tel Aviv be 27°C on November | entrada 0.51, agora 0.60, LLM 0.20, edge 0.13, medium | Modelo 0.20 vs mercado 0.47
- YES Will Аndrey Gyurov win the next Bulgarian presidential elect | entrada 0.35, agora 0.32, LLM 0.52, edge 0.08, medium | Market underprices Gyurov's chances given broad establishment endorsements from former PMs and presi
- YES Will voter turnout in the second round of the 2026 Bulgaria  | entrada 0.19, agora 0.17, LLM 0.35, edge 0.07, medium | The market underestimates the compounding effect of voter apathy and fatigue from consecutive rounds
- YES Will the highest temperature in Paris be 13°C on November 1? | entrada 0.44, agora 0.44, LLM 0.18, edge 0.11, medium | Modelo 0.18 vs mercado 0.41
- YES Will the highest temperature in Hong Kong be 28°C on Novembe | entrada 0.50, agora 0.50, LLM 0.20, edge 0.15, medium | Modelo 0.20 vs mercado 0.48
- YES Will the highest temperature in Karachi be 36°C on November  | entrada 0.51, agora 0.51, LLM 0.17, edge 0.14, medium | Modelo 0.17 vs mercado 0.47
- YES Will the highest temperature in Houston be between 84-85°F o | entrada 0.51, agora 0.51, LLM 0.20, edge 0.14, medium | Modelo 0.20 vs mercado 0.48

## Ultimas 10 fechadas
- YES Will the highest temperature in Cape Town be 21°C  | take-profit | $+3.48 | 6.3h
- YES Will the highest temperature in Madrid be 22°C on  | stop-loss | $-5.21 | 6.3h
- YES Will the highest temperature in Paris be 15°C on O | take-profit | $+5.49 | 12.3h
- YES Will the highest temperature in Milan be 17°C on O | take-profit | $+6.28 | 12.3h
- YES Will the highest temperature in Singapore be 33°C  | take-profit | $+13.97 | 18.2h
- YES Will the highest temperature in Tokyo be 23°C on O | take-profit | $+14.45 | 18.2h
- YES Will the highest temperature in Shenzhen be 30°C o | take-profit | $+4.66 | 18.2h
- YES Will the highest temperature in Tel Aviv be 27°C o | stop-loss | $-5.62 | 7.0h
- YES Will the highest temperature in Wellington be 14°C | stop-loss | $-10.79 | 12.2h
- YES Will the highest temperature in Houston be between | take-profit | $+13.53 | 22.2h
