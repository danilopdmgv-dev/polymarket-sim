# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-11-02 02:03 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1243.27 (-37.8%) | **Cash:** $1163.76 | **Abertas:** 6 | **Ciclos:** 61
**Fechadas:** 107 | **Win rate:** 31% | **PnL realizado:** $-755.45
**Chamadas ao LLM hoje:** 8

## Por motivo de saida
- resolvido: 1 trades, PnL $-46.54
- stop-loss: 73 trades, PnL $-1290.65
- take-profit: 33 trades, PnL $+581.74

## Por categoria
- Clima: 94 trades, win 30%, PnL $-733.51
- Outros: 2 trades, win 50%, PnL $+4.14
- Politica: 11 trades, win 36%, PnL $-26.08
- **Clima INVERSO (compra o lado oposto ao modelo):** 45 trades, win 44%, PnL $-16.99

## Calibracao do LLM vs mercado (361 mercados resolvidos)
- Brier LLM: 0.2974 | Brier mercado: 0.2207 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (261): LLM 0.3401 vs mercado 0.2326
  - Economia/Dados (7): LLM 0.1220 vs mercado 0.1228
  - Entretenimento (23): LLM 0.1428 vs mercado 0.1476
  - Outros (37): LLM 0.1838 vs mercado 0.1822
  - Politica (33): LLM 0.2320 vs mercado 0.2419
- Fonte clima (261): modelo 0.3401 vs mercado 0.2326 -> PERDENDO
- Fonte llm (100): modelo 0.1859 vs mercado 0.1898 -> GANHANDO
- Clima (242): sigma largo 0.3467 | sigma estreito 0.3211 | mercado 0.2341

## Posicoes abertas
- YES Will the highest temperature in Amsterdam be 13°C on Novembe | entrada 0.60, agora 0.71, LLM 0.23, edge 0.18, medium | Modelo 0.23 vs mercado 0.57
- YES Will the highest temperature in London be 13°C on November 2 | entrada 0.51, agora 0.41, LLM 0.21, edge 0.13, medium | Modelo 0.21 vs mercado 0.48
- YES Will the highest temperature in Cape Town be 21°C on Novembe | entrada 0.59, agora 0.50, LLM 0.21, edge 0.19, medium | Modelo 0.21 vs mercado 0.56
- YES Will the highest temperature in Miami be between 80-81°F on  | entrada 0.47, agora 0.50, LLM 0.19, edge 0.13, medium | Modelo 0.19 vs mercado 0.45
- YES Will the highest temperature in Austin be between 84-85°F on | entrada 0.57, agora 0.57, LLM 0.19, edge 0.18, medium | Modelo 0.19 vs mercado 0.55
- YES Will the highest temperature in Busan be 18°C on November 3? | entrada 0.41, agora 0.41, LLM 0.20, edge 0.09, medium | Modelo 0.20 vs mercado 0.39

## Ultimas 10 fechadas
- YES Will the highest temperature in Singapore be 32°C  | stop-loss | $-4.60 | 6.7h
- YES Will the highest temperature in Munich be 7°C on N | stop-loss | $-6.76 | 11.4h
- NO Will Iliana Iotova win the second round of the 202 | stop-loss | $-47.78 | 3.6h
- YES Will the highest temperature in Paris be 12°C on N | stop-loss | $-6.84 | 8.3h
- YES Will the highest temperature in Helsinki be 9°C on | stop-loss | $-5.00 | 4.7h
- YES Will the highest temperature in Houston be between | stop-loss | $-8.62 | 29.0h
- YES Will the highest temperature in London be 12°C on  | stop-loss | $-13.55 | 6.9h
- YES Will the highest temperature in Munich be 9°C on N | stop-loss | $-13.60 | 6.9h
- YES Will the highest temperature in Jeddah be 35°C on  | take-profit | $+13.85 | 20.0h
- YES Will the highest temperature in Moscow be 10°C on  | take-profit | $+15.78 | 20.0h
