# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-11-03 01:57 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1203.51 (-39.8%) | **Cash:** $1002.46 | **Abertas:** 9 | **Ciclos:** 64
**Fechadas:** 114 | **Win rate:** 30% | **PnL realizado:** $-797.87
**Chamadas ao LLM hoje:** 10

## Por motivo de saida
- resolvido: 1 trades, PnL $-46.54
- stop-loss: 79 trades, PnL $-1341.96
- take-profit: 34 trades, PnL $+590.62

## Por categoria
- Clima: 101 trades, win 29%, PnL $-775.94
- Outros: 2 trades, win 50%, PnL $+4.14
- Politica: 11 trades, win 36%, PnL $-26.08
- **Clima INVERSO (compra o lado oposto ao modelo):** 52 trades, win 40%, PnL $-59.42

## Calibracao do LLM vs mercado (408 mercados resolvidos)
- Brier LLM: 0.3013 | Brier mercado: 0.2218 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (301): LLM 0.3441 vs mercado 0.2352
  - Economia/Dados (7): LLM 0.1220 vs mercado 0.1228
  - Entretenimento (23): LLM 0.1428 vs mercado 0.1476
  - Outros (40): LLM 0.1759 vs mercado 0.1737
  - Politica (37): LLM 0.2215 vs mercado 0.2302
- Fonte clima (301): modelo 0.3441 vs mercado 0.2352 -> PERDENDO
- Fonte llm (107): modelo 0.1810 vs mercado 0.1843 -> GANHANDO
- Clima (282): sigma largo 0.3500 | sigma estreito 0.3208 | mercado 0.2367

## Posicoes abertas
- YES Will the highest temperature in Busan be 18°C on November 3? | entrada 0.41, agora 0.42, LLM 0.20, edge 0.09, medium | Modelo 0.20 vs mercado 0.39
- YES Will the highest temperature in Hong Kong be 28°C on Novembe | entrada 0.53, agora 0.47, LLM 0.21, edge 0.13, medium | Modelo 0.21 vs mercado 0.49
- YES Will the Republicans win the Texas Senate race in 2026? | entrada 0.26, agora 0.26, LLM 0.78, edge 0.25, medium | The market overreacts to late Democratic enthusiasm and polls, underestimating the durable structura
- NO Will the Democrats win the Texas Senate race in 2026? | entrada 0.25, agora 0.27, LLM 0.23, edge 0.25, medium | O mercado superestima a onda democrata nacional ignorando o histórico republicano profundo do Texas.
- YES Will the highest temperature in New York City be between 70- | entrada 0.41, agora 0.33, LLM 0.19, edge 0.08, medium | Modelo 0.19 vs mercado 0.38
- YES Will the highest temperature in Dallas be between 74-75°F on | entrada 0.44, agora 0.50, LLM 0.23, edge 0.09, medium | Modelo 0.23 vs mercado 0.42
- YES Will the highest temperature in London be 13°C on November 3 | entrada 0.52, agora 0.52, LLM 0.26, edge 0.11, medium | Modelo 0.26 vs mercado 0.49
- YES Will the highest temperature in Tel Aviv be 28°C on November | entrada 0.65, agora 0.65, LLM 0.27, edge 0.18, medium | Modelo 0.27 vs mercado 0.61
- YES US x Iran ceasefire continues through November 2? | entrada 0.51, agora 0.51, LLM 0.95, edge 0.21, high | The market is lagging behind the literal expiration time, failing to fully price in that the deadlin

## Ultimas 10 fechadas
- YES Will the highest temperature in Madrid be 16°C on  | stop-loss | $-6.61 | 6.0h
- YES Will the highest temperature in Tel Aviv be 27°C o | stop-loss | $-4.11 | 6.0h
- YES Will the highest temperature in Austin be between  | stop-loss | $-9.79 | 17.9h
- YES Will the highest temperature in Miami be between 8 | stop-loss | $-12.86 | 21.0h
- YES Will the highest temperature in Cape Town be 21°C  | take-profit | $+8.88 | 24.6h
- YES Will the highest temperature in Amsterdam be 13°C  | stop-loss | $-13.69 | 29.3h
- YES Will the highest temperature in London be 13°C on  | stop-loss | $-4.24 | 19.1h
- YES Will the highest temperature in Singapore be 32°C  | stop-loss | $-4.60 | 6.7h
- YES Will the highest temperature in Munich be 7°C on N | stop-loss | $-6.76 | 11.4h
- NO Will Iliana Iotova win the second round of the 202 | stop-loss | $-47.78 | 3.6h
