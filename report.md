# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-11-01 07:47 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1322.68 (-33.9%) | **Cash:** $1203.41 | **Abertas:** 7 | **Ciclos:** 57
**Fechadas:** 95 | **Win rate:** 32% | **PnL realizado:** $-674.17
**Chamadas ao LLM hoje:** 15

## Por motivo de saida
- resolvido: 1 trades, PnL $-46.54
- stop-loss: 64 trades, PnL $-1164.79
- take-profit: 30 trades, PnL $+537.16

## Por categoria
- Clima: 84 trades, win 30%, PnL $-719.13
- Outros: 2 trades, win 50%, PnL $+4.14
- Politica: 9 trades, win 44%, PnL $+40.81
- **Clima INVERSO (compra o lado oposto ao modelo):** 35 trades, win 49%, PnL $-2.61

## Calibracao do LLM vs mercado (317 mercados resolvidos)
- Brier LLM: 0.2965 | Brier mercado: 0.2176 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (237): LLM 0.3390 vs mercado 0.2317
  - Economia/Dados (6): LLM 0.0559 vs mercado 0.0628
  - Entretenimento (17): LLM 0.1604 vs mercado 0.1664
  - Outros (26): LLM 0.1436 vs mercado 0.1397
  - Politica (31): LLM 0.2217 vs mercado 0.2335
- Fonte clima (237): modelo 0.3390 vs mercado 0.2317 -> PERDENDO
- Fonte llm (80): modelo 0.1709 vs mercado 0.1759 -> GANHANDO
- Clima (218): sigma largo 0.3461 | sigma estreito 0.3210 | mercado 0.2333

## Posicoes abertas
- YES Will Аndrey Gyurov win the next Bulgarian presidential elect | entrada 0.35, agora 0.34, LLM 0.52, edge 0.08, medium | Market underprices Gyurov's chances given broad establishment endorsements from former PMs and presi
- YES Will the highest temperature in Paris be 13°C on November 1? | entrada 0.44, agora 0.38, LLM 0.18, edge 0.11, medium | Modelo 0.18 vs mercado 0.41
- YES Will the highest temperature in Houston be between 84-85°F o | entrada 0.51, agora 0.51, LLM 0.20, edge 0.14, medium | Modelo 0.20 vs mercado 0.48
- YES Will the highest temperature in Moscow be 10°C on November 1 | entrada 0.45, agora 0.43, LLM 0.17, edge 0.14, medium | Modelo 0.17 vs mercado 0.43
- YES Will the highest temperature in Jeddah be 35°C on November 1 | entrada 0.48, agora 0.49, LLM 0.16, edge 0.16, medium | Modelo 0.16 vs mercado 0.46
- YES Will the highest temperature in Munich be 9°C on November 1? | entrada 0.48, agora 0.48, LLM 0.20, edge 0.13, medium | Modelo 0.20 vs mercado 0.46
- YES Will the highest temperature in London be 12°C on November 1 | entrada 0.41, agora 0.41, LLM 0.19, edge 0.09, medium | Modelo 0.19 vs mercado 0.38

## Ultimas 10 fechadas
- YES Will the highest temperature in Tokyo be 20°C on N | take-profit | $+11.57 | 9.7h
- YES Will the highest temperature in Karachi be 36°C on | stop-loss | $-10.56 | 17.5h
- YES Will voter turnout in the second round of the 2026 | stop-loss | $-8.24 | 17.3h
- YES Will the highest temperature in Hong Kong be 28°C  | stop-loss | $-5.02 | 7.8h
- YES Will the highest temperature in Tel Aviv be 27°C o | take-profit | $+2.68 | 10.7h
- YES Will the highest temperature in Buenos Aires be 26 | take-profit | $+17.29 | 19.9h
- YES Will the highest temperature in Cape Town be 21°C  | take-profit | $+3.48 | 6.3h
- YES Will the highest temperature in Madrid be 22°C on  | stop-loss | $-5.21 | 6.3h
- YES Will the highest temperature in Paris be 15°C on O | take-profit | $+5.49 | 12.3h
- YES Will the highest temperature in Milan be 17°C on O | take-profit | $+6.28 | 12.3h
