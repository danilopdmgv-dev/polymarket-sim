# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-11-01 19:19 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1304.59 (-34.8%) | **Cash:** $1175.27 | **Abertas:** 7 | **Ciclos:** 59
**Fechadas:** 103 | **Win rate:** 32% | **PnL realizado:** $-689.47
**Chamadas ao LLM hoje:** 30

## Por motivo de saida
- resolvido: 1 trades, PnL $-46.54
- stop-loss: 69 trades, PnL $-1224.67
- take-profit: 33 trades, PnL $+581.74

## Por categoria
- Clima: 91 trades, win 31%, PnL $-715.31
- Outros: 2 trades, win 50%, PnL $+4.14
- Politica: 10 trades, win 40%, PnL $+21.70
- **Clima INVERSO (compra o lado oposto ao modelo):** 42 trades, win 48%, PnL $+1.20

## Calibracao do LLM vs mercado (343 mercados resolvidos)
- Brier LLM: 0.2958 | Brier mercado: 0.2177 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (250): LLM 0.3413 vs mercado 0.2322
  - Economia/Dados (6): LLM 0.0559 vs mercado 0.0628
  - Entretenimento (23): LLM 0.1428 vs mercado 0.1476
  - Outros (32): LLM 0.1524 vs mercado 0.1520
  - Politica (32): LLM 0.2390 vs mercado 0.2492
- Fonte clima (250): modelo 0.3413 vs mercado 0.2322 -> PERDENDO
- Fonte llm (93): modelo 0.1736 vs mercado 0.1786 -> GANHANDO
- Clima (231): sigma largo 0.3482 | sigma estreito 0.3240 | mercado 0.2339

## Posicoes abertas
- YES Will the highest temperature in Paris be 12°C on November 2? | entrada 0.50, agora 0.41, LLM 0.20, edge 0.14, medium | Modelo 0.20 vs mercado 0.47
- YES Will the highest temperature in Amsterdam be 13°C on Novembe | entrada 0.60, agora 0.58, LLM 0.23, edge 0.18, medium | Modelo 0.23 vs mercado 0.57
- YES Will the highest temperature in Munich be 7°C on November 2? | entrada 0.54, agora 0.46, LLM 0.21, edge 0.17, medium | Modelo 0.21 vs mercado 0.53
- YES Will the highest temperature in London be 13°C on November 2 | entrada 0.51, agora 0.47, LLM 0.21, edge 0.13, medium | Modelo 0.21 vs mercado 0.48
- YES Will the highest temperature in Singapore be 32°C on Novembe | entrada 0.49, agora 0.49, LLM 0.26, edge 0.11, medium | Modelo 0.26 vs mercado 0.47
- YES Will the highest temperature in Cape Town be 21°C on Novembe | entrada 0.59, agora 0.59, LLM 0.21, edge 0.19, medium | Modelo 0.21 vs mercado 0.56
- NO Will Iliana Iotova win the second round of the 2026 Bulgaria | entrada 0.12, agora 0.12, LLM 0.15, edge 0.35, high | Market overprices the 12% threshold given current exit poll margins hovering around 9%.

## Ultimas 10 fechadas
- YES Will the highest temperature in Helsinki be 9°C on | stop-loss | $-5.00 | 4.7h
- YES Will the highest temperature in Houston be between | stop-loss | $-8.62 | 29.0h
- YES Will the highest temperature in London be 12°C on  | stop-loss | $-13.55 | 6.9h
- YES Will the highest temperature in Munich be 9°C on N | stop-loss | $-13.60 | 6.9h
- YES Will the highest temperature in Jeddah be 35°C on  | take-profit | $+13.85 | 20.0h
- YES Will the highest temperature in Moscow be 10°C on  | take-profit | $+15.78 | 20.0h
- YES Will the highest temperature in Paris be 13°C on N | take-profit | $+14.96 | 24.3h
- YES Will Аndrey Gyurov win the next Bulgarian presiden | stop-loss | $-19.11 | 30.7h
- YES Will the highest temperature in Tokyo be 20°C on N | take-profit | $+11.57 | 9.7h
- YES Will the highest temperature in Karachi be 36°C on | stop-loss | $-10.56 | 17.5h
