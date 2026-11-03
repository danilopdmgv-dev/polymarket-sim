# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-11-03 08:58 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1190.55 (-40.5%) | **Cash:** $1043.56 | **Abertas:** 8 | **Ciclos:** 65
**Fechadas:** 120 | **Win rate:** 30% | **PnL realizado:** $-806.52
**Chamadas ao LLM hoje:** 19

## Por motivo de saida
- resolvido: 1 trades, PnL $-46.54
- stop-loss: 83 trades, PnL $-1379.99
- take-profit: 36 trades, PnL $+620.00

## Por categoria
- Clima: 106 trades, win 28%, PnL $-803.05
- Outros: 2 trades, win 50%, PnL $+4.14
- Politica: 12 trades, win 42%, PnL $-7.62
- **Clima INVERSO (compra o lado oposto ao modelo):** 57 trades, win 39%, PnL $-86.53

## Calibracao do LLM vs mercado (421 mercados resolvidos)
- Brier LLM: 0.3036 | Brier mercado: 0.2224 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (314): LLM 0.3454 vs mercado 0.2354
  - Economia/Dados (7): LLM 0.1220 vs mercado 0.1228
  - Entretenimento (23): LLM 0.1428 vs mercado 0.1476
  - Outros (40): LLM 0.1759 vs mercado 0.1737
  - Politica (37): LLM 0.2215 vs mercado 0.2302
- Fonte clima (314): modelo 0.3454 vs mercado 0.2354 -> PERDENDO
- Fonte llm (107): modelo 0.1810 vs mercado 0.1843 -> GANHANDO
- Clima (295): sigma largo 0.3511 | sigma estreito 0.3214 | mercado 0.2369

## Posicoes abertas
- YES Will the Republicans win the Texas Senate race in 2026? | entrada 0.26, agora 0.25, LLM 0.78, edge 0.25, medium | The market overreacts to late Democratic enthusiasm and polls, underestimating the durable structura
- NO Will the Democrats win the Texas Senate race in 2026? | entrada 0.25, agora 0.25, LLM 0.23, edge 0.25, medium | O mercado superestima a onda democrata nacional ignorando o histórico republicano profundo do Texas.
- YES Will the highest temperature in Tel Aviv be 28°C on November | entrada 0.65, agora 0.57, LLM 0.27, edge 0.18, medium | Modelo 0.27 vs mercado 0.61
- YES Will the highest temperature in London be 12°C on November 4 | entrada 0.42, agora 0.42, LLM 0.20, edge 0.09, medium | Modelo 0.20 vs mercado 0.40
- YES Will the highest temperature in Singapore be 32°C on Novembe | entrada 0.41, agora 0.41, LLM 0.16, edge 0.11, medium | Modelo 0.16 vs mercado 0.39
- YES Will the highest temperature in Tel Aviv be 28°C on November | entrada 0.48, agora 0.48, LLM 0.18, edge 0.15, medium | Modelo 0.18 vs mercado 0.47
- YES Will the highest temperature in Denver be between 54-55°F on | entrada 0.59, agora 0.59, LLM 0.32, edge 0.12, medium | Modelo 0.32 vs mercado 0.56
- YES Will the highest temperature in Paris be 11°C on November 4? | entrada 0.40, agora 0.40, LLM 0.19, edge 0.10, medium | Modelo 0.19 vs mercado 0.38

## Ultimas 10 fechadas
- YES US x Iran ceasefire continues through November 2? | take-profit | $+18.46 | 7.0h
- YES Will the highest temperature in London be 13°C on  | stop-loss | $-8.62 | 7.0h
- YES Will the highest temperature in Dallas be between  | stop-loss | $-12.38 | 13.0h
- YES Will the highest temperature in New York City be b | stop-loss | $-4.29 | 13.0h
- YES Will the highest temperature in Hong Kong be 28°C  | take-profit | $+10.92 | 23.2h
- YES Will the highest temperature in Busan be 18°C on N | stop-loss | $-12.73 | 30.9h
- YES Will the highest temperature in Madrid be 16°C on  | stop-loss | $-6.61 | 6.0h
- YES Will the highest temperature in Tel Aviv be 27°C o | stop-loss | $-4.11 | 6.0h
- YES Will the highest temperature in Austin be between  | stop-loss | $-9.79 | 17.9h
- YES Will the highest temperature in Miami be between 8 | stop-loss | $-12.86 | 21.0h
