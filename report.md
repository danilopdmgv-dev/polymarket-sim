# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-11-01 22:58 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1251.42 (-37.4%) | **Cash:** $1173.61 | **Abertas:** 6 | **Ciclos:** 60
**Fechadas:** 105 | **Win rate:** 31% | **PnL realizado:** $-744.09
**Chamadas ao LLM hoje:** 36

## Por motivo de saida
- resolvido: 1 trades, PnL $-46.54
- stop-loss: 71 trades, PnL $-1279.29
- take-profit: 33 trades, PnL $+581.74

## Por categoria
- Clima: 92 trades, win 30%, PnL $-722.15
- Outros: 2 trades, win 50%, PnL $+4.14
- Politica: 11 trades, win 36%, PnL $-26.08
- **Clima INVERSO (compra o lado oposto ao modelo):** 43 trades, win 47%, PnL $-5.63

## Calibracao do LLM vs mercado (353 mercados resolvidos)
- Brier LLM: 0.2999 | Brier mercado: 0.2205 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (253): LLM 0.3450 vs mercado 0.2326
  - Economia/Dados (7): LLM 0.1220 vs mercado 0.1228
  - Entretenimento (23): LLM 0.1428 vs mercado 0.1476
  - Outros (37): LLM 0.1838 vs mercado 0.1822
  - Politica (33): LLM 0.2320 vs mercado 0.2419
- Fonte clima (253): modelo 0.3450 vs mercado 0.2326 -> PERDENDO
- Fonte llm (100): modelo 0.1859 vs mercado 0.1898 -> GANHANDO
- Clima (234): sigma largo 0.3522 | sigma estreito 0.3265 | mercado 0.2342

## Posicoes abertas
- YES Will the highest temperature in Amsterdam be 13°C on Novembe | entrada 0.60, agora 0.66, LLM 0.23, edge 0.18, medium | Modelo 0.23 vs mercado 0.57
- YES Will the highest temperature in Munich be 7°C on November 2? | entrada 0.54, agora 0.50, LLM 0.21, edge 0.17, medium | Modelo 0.21 vs mercado 0.53
- YES Will the highest temperature in London be 13°C on November 2 | entrada 0.51, agora 0.48, LLM 0.21, edge 0.13, medium | Modelo 0.21 vs mercado 0.48
- YES Will the highest temperature in Singapore be 32°C on Novembe | entrada 0.49, agora 0.44, LLM 0.26, edge 0.11, medium | Modelo 0.26 vs mercado 0.47
- YES Will the highest temperature in Cape Town be 21°C on Novembe | entrada 0.59, agora 0.47, LLM 0.21, edge 0.19, medium | Modelo 0.21 vs mercado 0.56
- YES Will the highest temperature in Miami be between 80-81°F on  | entrada 0.47, agora 0.47, LLM 0.19, edge 0.13, medium | Modelo 0.19 vs mercado 0.45

## Ultimas 10 fechadas
- NO Will Iliana Iotova win the second round of the 202 | stop-loss | $-47.78 | 3.6h
- YES Will the highest temperature in Paris be 12°C on N | stop-loss | $-6.84 | 8.3h
- YES Will the highest temperature in Helsinki be 9°C on | stop-loss | $-5.00 | 4.7h
- YES Will the highest temperature in Houston be between | stop-loss | $-8.62 | 29.0h
- YES Will the highest temperature in London be 12°C on  | stop-loss | $-13.55 | 6.9h
- YES Will the highest temperature in Munich be 9°C on N | stop-loss | $-13.60 | 6.9h
- YES Will the highest temperature in Jeddah be 35°C on  | take-profit | $+13.85 | 20.0h
- YES Will the highest temperature in Moscow be 10°C on  | take-profit | $+15.78 | 20.0h
- YES Will the highest temperature in Paris be 13°C on N | take-profit | $+14.96 | 24.3h
- YES Will Аndrey Gyurov win the next Bulgarian presiden | stop-loss | $-19.11 | 30.7h
