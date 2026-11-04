# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-11-04 23:50 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1083.20 (-45.8%) | **Cash:** $1021.18 | **Abertas:** 6 | **Ciclos:** 70
**Fechadas:** 134 | **Win rate:** 31% | **PnL realizado:** $-910.73
**Chamadas ao LLM hoje:** 22

## Por motivo de saida
- resolvido: 3 trades, PnL $-62.42
- stop-loss: 90 trades, PnL $-1503.40
- take-profit: 41 trades, PnL $+655.10

## Por categoria
- Clima: 117 trades, win 31%, PnL $-801.58
- Outros: 2 trades, win 50%, PnL $+4.14
- Politica: 15 trades, win 33%, PnL $-113.30
- **Clima INVERSO (compra o lado oposto ao modelo):** 68 trades, win 41%, PnL $-85.06

## Calibracao do LLM vs mercado (482 mercados resolvidos)
- Brier LLM: 0.3066 | Brier mercado: 0.2224 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (364): LLM 0.3440 vs mercado 0.2354
  - Economia/Dados (7): LLM 0.1220 vs mercado 0.1228
  - Entretenimento (27): LLM 0.1621 vs mercado 0.1673
  - Outros (40): LLM 0.1759 vs mercado 0.1737
  - Politica (44): LLM 0.2346 vs mercado 0.2091
- Fonte clima (364): modelo 0.3440 vs mercado 0.2354 -> PERDENDO
- Fonte llm (118): modelo 0.1914 vs mercado 0.1824 -> PERDENDO
- Clima (345): sigma largo 0.3488 | sigma estreito 0.3213 | mercado 0.2367

## Posicoes abertas
- YES Will the highest temperature in Houston be between 82-83°F o | entrada 0.47, agora 0.45, LLM 0.10, edge 0.19, medium | Modelo 0.10 vs mercado 0.45
- YES Will the highest temperature in London be 11°C on November 5 | entrada 0.62, agora 0.53, LLM 0.22, edge 0.21, medium | Modelo 0.22 vs mercado 0.60
- YES Will the highest temperature in Dallas be between 78-79°F on | entrada 0.59, agora 0.51, LLM 0.18, edge 0.21, medium | Modelo 0.18 vs mercado 0.57
- YES Will the highest temperature in New York City be between 70- | entrada 0.52, agora 0.45, LLM 0.21, edge 0.15, medium | Modelo 0.21 vs mercado 0.50
- YES Will the highest temperature in Miami be between 84-85°F on  | entrada 0.41, agora 0.38, LLM 0.19, edge 0.09, medium | Modelo 0.19 vs mercado 0.38
- YES Will the highest temperature in Lucknow be 31°C on November  | entrada 0.41, agora 0.41, LLM 0.18, edge 0.09, medium | Modelo 0.18 vs mercado 0.38

## Ultimas 10 fechadas
- YES Will the highest temperature in Houston be between | take-profit | $+9.68 | 21.3h
- NO Will the Democrats win the Iowa Senate race in 202 | resolvido | $-33.83 | 15.6h
- YES Will the highest temperature in Karachi be 35°C on | stop-loss | $-12.15 | 20.0h
- YES Will the highest temperature in Paris be 10°C on N | stop-loss | $-12.23 | 20.0h
- YES Will the highest temperature in London be 11°C on  | stop-loss | $-12.26 | 20.0h
- YES Will the highest temperature in Hong Kong be 28°C  | take-profit | $+9.50 | 25.3h
- YES Will the highest temperature in Singapore be 32°C  | resolvido | $+17.95 | 33.2h
- YES Will the highest temperature in Tel Aviv be 28°C o | take-profit | $+4.01 | 17.6h
- NO Will the Democrats win the Texas Senate race in 20 | stop-loss | $-35.89 | 40.7h
- YES Will the Republicans win the Texas Senate race in  | stop-loss | $-35.95 | 40.8h
