# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-11-02 20:01 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1206.53 (-39.7%) | **Cash:** $1061.26 | **Abertas:** 8 | **Ciclos:** 63
**Fechadas:** 112 | **Win rate:** 30% | **PnL realizado:** $-787.15
**Chamadas ao LLM hoje:** 26

## Por motivo de saida
- resolvido: 1 trades, PnL $-46.54
- stop-loss: 77 trades, PnL $-1331.23
- take-profit: 34 trades, PnL $+590.62

## Por categoria
- Clima: 99 trades, win 29%, PnL $-765.21
- Outros: 2 trades, win 50%, PnL $+4.14
- Politica: 11 trades, win 36%, PnL $-26.08
- **Clima INVERSO (compra o lado oposto ao modelo):** 50 trades, win 42%, PnL $-48.70

## Calibracao do LLM vs mercado (395 mercados resolvidos)
- Brier LLM: 0.2990 | Brier mercado: 0.2220 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (292): LLM 0.3406 vs mercado 0.2350
  - Economia/Dados (7): LLM 0.1220 vs mercado 0.1228
  - Entretenimento (23): LLM 0.1428 vs mercado 0.1476
  - Outros (38): LLM 0.1802 vs mercado 0.1789
  - Politica (35): LLM 0.2195 vs mercado 0.2290
- Fonte clima (292): modelo 0.3406 vs mercado 0.2350 -> PERDENDO
- Fonte llm (103): modelo 0.1812 vs mercado 0.1851 -> GANHANDO
- Clima (273): sigma largo 0.3464 | sigma estreito 0.3192 | mercado 0.2366

## Posicoes abertas
- YES Will the highest temperature in Busan be 18°C on November 3? | entrada 0.41, agora 0.42, LLM 0.20, edge 0.09, medium | Modelo 0.20 vs mercado 0.39
- YES Will the highest temperature in Hong Kong be 28°C on Novembe | entrada 0.53, agora 0.43, LLM 0.21, edge 0.13, medium | Modelo 0.21 vs mercado 0.49
- YES Will the Republicans win the Texas Senate race in 2026? | entrada 0.26, agora 0.24, LLM 0.78, edge 0.25, medium | The market overreacts to late Democratic enthusiasm and polls, underestimating the durable structura
- NO Will the Democrats win the Texas Senate race in 2026? | entrada 0.25, agora 0.24, LLM 0.23, edge 0.25, medium | O mercado superestima a onda democrata nacional ignorando o histórico republicano profundo do Texas.
- YES Will the highest temperature in Tel Aviv be 27°C on November | entrada 0.41, agora 0.41, LLM 0.22, edge 0.09, medium | Modelo 0.22 vs mercado 0.40
- YES Will the highest temperature in New York City be between 70- | entrada 0.41, agora 0.41, LLM 0.19, edge 0.08, medium | Modelo 0.19 vs mercado 0.38
- YES Will the highest temperature in Dallas be between 74-75°F on | entrada 0.44, agora 0.44, LLM 0.23, edge 0.09, medium | Modelo 0.23 vs mercado 0.42
- YES Will the highest temperature in Madrid be 16°C on November 3 | entrada 0.36, agora 0.36, LLM 0.14, edge 0.11, medium | Modelo 0.14 vs mercado 0.34

## Ultimas 10 fechadas
- YES Will the highest temperature in Austin be between  | stop-loss | $-9.79 | 17.9h
- YES Will the highest temperature in Miami be between 8 | stop-loss | $-12.86 | 21.0h
- YES Will the highest temperature in Cape Town be 21°C  | take-profit | $+8.88 | 24.6h
- YES Will the highest temperature in Amsterdam be 13°C  | stop-loss | $-13.69 | 29.3h
- YES Will the highest temperature in London be 13°C on  | stop-loss | $-4.24 | 19.1h
- YES Will the highest temperature in Singapore be 32°C  | stop-loss | $-4.60 | 6.7h
- YES Will the highest temperature in Munich be 7°C on N | stop-loss | $-6.76 | 11.4h
- NO Will Iliana Iotova win the second round of the 202 | stop-loss | $-47.78 | 3.6h
- YES Will the highest temperature in Paris be 12°C on N | stop-loss | $-6.84 | 8.3h
- YES Will the highest temperature in Helsinki be 9°C on | stop-loss | $-5.00 | 4.7h
