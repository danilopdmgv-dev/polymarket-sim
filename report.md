# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-11-01 14:40 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1325.92 (-33.7%) | **Cash:** $1240.74 | **Abertas:** 6 | **Ciclos:** 58
**Fechadas:** 101 | **Win rate:** 33% | **PnL realizado:** $-675.84
**Chamadas ao LLM hoje:** 22

## Por motivo de saida
- resolvido: 1 trades, PnL $-46.54
- stop-loss: 67 trades, PnL $-1211.04
- take-profit: 33 trades, PnL $+581.74

## Por categoria
- Clima: 89 trades, win 31%, PnL $-701.69
- Outros: 2 trades, win 50%, PnL $+4.14
- Politica: 10 trades, win 40%, PnL $+21.70
- **Clima INVERSO (compra o lado oposto ao modelo):** 40 trades, win 50%, PnL $+14.83

## Calibracao do LLM vs mercado (332 mercados resolvidos)
- Brier LLM: 0.2984 | Brier mercado: 0.2176 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (250): LLM 0.3413 vs mercado 0.2322
  - Economia/Dados (6): LLM 0.0559 vs mercado 0.0628
  - Entretenimento (19): LLM 0.1478 vs mercado 0.1539
  - Outros (26): LLM 0.1436 vs mercado 0.1397
  - Politica (31): LLM 0.2217 vs mercado 0.2335
- Fonte clima (250): modelo 0.3413 vs mercado 0.2322 -> PERDENDO
- Fonte llm (82): modelo 0.1677 vs mercado 0.1728 -> GANHANDO
- Clima (231): sigma largo 0.3482 | sigma estreito 0.3240 | mercado 0.2339

## Posicoes abertas
- YES Will the highest temperature in Houston be between 84-85°F o | entrada 0.51, agora 0.57, LLM 0.20, edge 0.14, medium | Modelo 0.20 vs mercado 0.48
- YES Will the highest temperature in Paris be 12°C on November 2? | entrada 0.50, agora 0.50, LLM 0.20, edge 0.14, medium | Modelo 0.20 vs mercado 0.47
- YES Will the highest temperature in Helsinki be 9°C on November  | entrada 0.65, agora 0.65, LLM 0.21, edge 0.22, medium | Modelo 0.21 vs mercado 0.62
- YES Will the highest temperature in Amsterdam be 13°C on Novembe | entrada 0.60, agora 0.60, LLM 0.23, edge 0.18, medium | Modelo 0.23 vs mercado 0.57
- YES Will the highest temperature in Munich be 7°C on November 2? | entrada 0.54, agora 0.54, LLM 0.21, edge 0.17, medium | Modelo 0.21 vs mercado 0.53
- YES Will the highest temperature in London be 13°C on November 2 | entrada 0.51, agora 0.51, LLM 0.21, edge 0.13, medium | Modelo 0.21 vs mercado 0.48

## Ultimas 10 fechadas
- YES Will the highest temperature in London be 12°C on  | stop-loss | $-13.55 | 6.9h
- YES Will the highest temperature in Munich be 9°C on N | stop-loss | $-13.60 | 6.9h
- YES Will the highest temperature in Jeddah be 35°C on  | take-profit | $+13.85 | 20.0h
- YES Will the highest temperature in Moscow be 10°C on  | take-profit | $+15.78 | 20.0h
- YES Will the highest temperature in Paris be 13°C on N | take-profit | $+14.96 | 24.3h
- YES Will Аndrey Gyurov win the next Bulgarian presiden | stop-loss | $-19.11 | 30.7h
- YES Will the highest temperature in Tokyo be 20°C on N | take-profit | $+11.57 | 9.7h
- YES Will the highest temperature in Karachi be 36°C on | stop-loss | $-10.56 | 17.5h
- YES Will voter turnout in the second round of the 2026 | stop-loss | $-8.24 | 17.3h
- YES Will the highest temperature in Hong Kong be 28°C  | stop-loss | $-5.02 | 7.8h
