# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-11-03 22:12 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1184.58 (-40.8%) | **Cash:** $1040.76 | **Abertas:** 8 | **Ciclos:** 67
**Fechadas:** 124 | **Win rate:** 31% | **PnL realizado:** $-809.54
**Chamadas ao LLM hoje:** 39

## Por motivo de saida
- resolvido: 1 trades, PnL $-46.54
- stop-loss: 85 trades, PnL $-1394.92
- take-profit: 38 trades, PnL $+631.91

## Por categoria
- Clima: 110 trades, win 29%, PnL $-806.07
- Outros: 2 trades, win 50%, PnL $+4.14
- Politica: 12 trades, win 42%, PnL $-7.62
- **Clima INVERSO (compra o lado oposto ao modelo):** 61 trades, win 39%, PnL $-89.55

## Calibracao do LLM vs mercado (447 mercados resolvidos)
- Brier LLM: 0.2981 | Brier mercado: 0.2197 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (331): LLM 0.3388 vs mercado 0.2339
  - Economia/Dados (7): LLM 0.1220 vs mercado 0.1228
  - Entretenimento (26): LLM 0.1406 vs mercado 0.1461
  - Outros (40): LLM 0.1759 vs mercado 0.1737
  - Politica (43): LLM 0.2221 vs mercado 0.2136
- Fonte clima (331): modelo 0.3388 vs mercado 0.2339 -> PERDENDO
- Fonte llm (116): modelo 0.1818 vs mercado 0.1792 -> PERDENDO
- Clima (312): sigma largo 0.3438 | sigma estreito 0.3159 | mercado 0.2352

## Posicoes abertas
- YES Will the Republicans win the Texas Senate race in 2026? | entrada 0.26, agora 0.23, LLM 0.78, edge 0.25, medium | The market overreacts to late Democratic enthusiasm and polls, underestimating the durable structura
- NO Will the Democrats win the Texas Senate race in 2026? | entrada 0.25, agora 0.23, LLM 0.23, edge 0.25, medium | O mercado superestima a onda democrata nacional ignorando o histórico republicano profundo do Texas.
- YES Will the highest temperature in Singapore be 32°C on Novembe | entrada 0.41, agora 0.40, LLM 0.16, edge 0.11, medium | Modelo 0.16 vs mercado 0.39
- YES Will the highest temperature in Tel Aviv be 28°C on November | entrada 0.48, agora 0.60, LLM 0.18, edge 0.15, medium | Modelo 0.18 vs mercado 0.47
- YES Will the highest temperature in Hong Kong be 28°C on Novembe | entrada 0.56, agora 0.50, LLM 0.25, edge 0.14, medium | Modelo 0.25 vs mercado 0.53
- YES Will the highest temperature in London be 11°C on November 4 | entrada 0.72, agora 0.72, LLM 0.21, edge 0.25, medium | Modelo 0.21 vs mercado 0.68
- YES Will the highest temperature in Paris be 10°C on November 4? | entrada 0.60, agora 0.60, LLM 0.23, edge 0.18, medium | Modelo 0.23 vs mercado 0.57
- YES Will the highest temperature in Karachi be 35°C on November  | entrada 0.43, agora 0.43, LLM 0.26, edge 0.06, medium | Modelo 0.26 vs mercado 0.41

## Ultimas 10 fechadas
- YES Will the highest temperature in Paris be 11°C on N | stop-loss | $-9.19 | 13.2h
- YES Will the highest temperature in Denver be between  | take-profit | $+5.62 | 13.2h
- YES Will the highest temperature in London be 12°C on  | stop-loss | $-5.73 | 13.2h
- YES Will the highest temperature in Tel Aviv be 28°C o | take-profit | $+6.29 | 14.9h
- YES US x Iran ceasefire continues through November 2? | take-profit | $+18.46 | 7.0h
- YES Will the highest temperature in London be 13°C on  | stop-loss | $-8.62 | 7.0h
- YES Will the highest temperature in Dallas be between  | stop-loss | $-12.38 | 13.0h
- YES Will the highest temperature in New York City be b | stop-loss | $-4.29 | 13.0h
- YES Will the highest temperature in Hong Kong be 28°C  | take-profit | $+10.92 | 23.2h
- YES Will the highest temperature in Busan be 18°C on N | stop-loss | $-12.73 | 30.9h
