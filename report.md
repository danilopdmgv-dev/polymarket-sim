# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-11-02 09:47 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1246.31 (-37.7%) | **Cash:** $1085.58 | **Abertas:** 8 | **Ciclos:** 62
**Fechadas:** 108 | **Win rate:** 31% | **PnL realizado:** $-759.69
**Chamadas ao LLM hoje:** 16

## Por motivo de saida
- resolvido: 1 trades, PnL $-46.54
- stop-loss: 74 trades, PnL $-1294.89
- take-profit: 33 trades, PnL $+581.74

## Por categoria
- Clima: 95 trades, win 29%, PnL $-737.75
- Outros: 2 trades, win 50%, PnL $+4.14
- Politica: 11 trades, win 36%, PnL $-26.08
- **Clima INVERSO (compra o lado oposto ao modelo):** 46 trades, win 43%, PnL $-21.23

## Calibracao do LLM vs mercado (378 mercados resolvidos)
- Brier LLM: 0.2974 | Brier mercado: 0.2212 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (275): LLM 0.3410 vs mercado 0.2348
  - Economia/Dados (7): LLM 0.1220 vs mercado 0.1228
  - Entretenimento (23): LLM 0.1428 vs mercado 0.1476
  - Outros (38): LLM 0.1802 vs mercado 0.1789
  - Politica (35): LLM 0.2195 vs mercado 0.2290
- Fonte clima (275): modelo 0.3410 vs mercado 0.2348 -> PERDENDO
- Fonte llm (103): modelo 0.1812 vs mercado 0.1851 -> GANHANDO
- Clima (256): sigma largo 0.3472 | sigma estreito 0.3221 | mercado 0.2364

## Posicoes abertas
- YES Will the highest temperature in Amsterdam be 13°C on Novembe | entrada 0.60, agora 0.70, LLM 0.23, edge 0.18, medium | Modelo 0.23 vs mercado 0.57
- YES Will the highest temperature in Cape Town be 21°C on Novembe | entrada 0.59, agora 0.65, LLM 0.21, edge 0.19, medium | Modelo 0.21 vs mercado 0.56
- YES Will the highest temperature in Miami be between 80-81°F on  | entrada 0.47, agora 0.55, LLM 0.19, edge 0.13, medium | Modelo 0.19 vs mercado 0.45
- YES Will the highest temperature in Austin be between 84-85°F on | entrada 0.57, agora 0.55, LLM 0.19, edge 0.18, medium | Modelo 0.19 vs mercado 0.55
- YES Will the highest temperature in Busan be 18°C on November 3? | entrada 0.41, agora 0.42, LLM 0.20, edge 0.09, medium | Modelo 0.20 vs mercado 0.39
- YES Will the highest temperature in Hong Kong be 28°C on Novembe | entrada 0.53, agora 0.53, LLM 0.21, edge 0.13, medium | Modelo 0.21 vs mercado 0.49
- YES Will the Republicans win the Texas Senate race in 2026? | entrada 0.26, agora 0.26, LLM 0.78, edge 0.25, medium | The market overreacts to late Democratic enthusiasm and polls, underestimating the durable structura
- NO Will the Democrats win the Texas Senate race in 2026? | entrada 0.25, agora 0.25, LLM 0.23, edge 0.25, medium | O mercado superestima a onda democrata nacional ignorando o histórico republicano profundo do Texas.

## Ultimas 10 fechadas
- YES Will the highest temperature in London be 13°C on  | stop-loss | $-4.24 | 19.1h
- YES Will the highest temperature in Singapore be 32°C  | stop-loss | $-4.60 | 6.7h
- YES Will the highest temperature in Munich be 7°C on N | stop-loss | $-6.76 | 11.4h
- NO Will Iliana Iotova win the second round of the 202 | stop-loss | $-47.78 | 3.6h
- YES Will the highest temperature in Paris be 12°C on N | stop-loss | $-6.84 | 8.3h
- YES Will the highest temperature in Helsinki be 9°C on | stop-loss | $-5.00 | 4.7h
- YES Will the highest temperature in Houston be between | stop-loss | $-8.62 | 29.0h
- YES Will the highest temperature in London be 12°C on  | stop-loss | $-13.55 | 6.9h
- YES Will the highest temperature in Munich be 9°C on N | stop-loss | $-13.60 | 6.9h
- YES Will the highest temperature in Jeddah be 35°C on  | take-profit | $+13.85 | 20.0h
