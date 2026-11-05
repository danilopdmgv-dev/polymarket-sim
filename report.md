# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-11-05 04:32 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1080.13 (-46.0%) | **Cash:** $1011.11 | **Abertas:** 6 | **Ciclos:** 71
**Fechadas:** 135 | **Win rate:** 31% | **PnL realizado:** $-920.83
**Chamadas ao LLM hoje:** 5

## Por motivo de saida
- resolvido: 3 trades, PnL $-62.42
- stop-loss: 91 trades, PnL $-1513.51
- take-profit: 41 trades, PnL $+655.10

## Por categoria
- Clima: 118 trades, win 31%, PnL $-811.68
- Outros: 2 trades, win 50%, PnL $+4.14
- Politica: 15 trades, win 33%, PnL $-113.30
- **Clima INVERSO (compra o lado oposto ao modelo):** 69 trades, win 41%, PnL $-95.17

## Calibracao do LLM vs mercado (495 mercados resolvidos)
- Brier LLM: 0.3010 | Brier mercado: 0.2183 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (364): LLM 0.3440 vs mercado 0.2354
  - Economia/Dados (7): LLM 0.1220 vs mercado 0.1228
  - Entretenimento (31): LLM 0.1449 vs mercado 0.1494
  - Outros (43): LLM 0.1639 vs mercado 0.1679
  - Politica (50): LLM 0.2281 vs mercado 0.1930
- Fonte clima (364): modelo 0.3440 vs mercado 0.2354 -> PERDENDO
- Fonte llm (131): modelo 0.1816 vs mercado 0.1707 -> PERDENDO
- Clima (345): sigma largo 0.3488 | sigma estreito 0.3213 | mercado 0.2367

## Posicoes abertas
- YES Will the highest temperature in Houston be between 82-83°F o | entrada 0.47, agora 0.57, LLM 0.10, edge 0.19, medium | Modelo 0.10 vs mercado 0.45
- YES Will the highest temperature in London be 11°C on November 5 | entrada 0.62, agora 0.66, LLM 0.22, edge 0.21, medium | Modelo 0.22 vs mercado 0.60
- YES Will the highest temperature in Dallas be between 78-79°F on | entrada 0.59, agora 0.55, LLM 0.18, edge 0.21, medium | Modelo 0.18 vs mercado 0.57
- YES Will the highest temperature in New York City be between 70- | entrada 0.52, agora 0.47, LLM 0.21, edge 0.15, medium | Modelo 0.21 vs mercado 0.50
- YES Will the highest temperature in Miami be between 84-85°F on  | entrada 0.41, agora 0.40, LLM 0.19, edge 0.09, medium | Modelo 0.19 vs mercado 0.38
- YES Will the highest temperature in Milan be 11°C on November 6? | entrada 0.46, agora 0.46, LLM 0.21, edge 0.11, medium | Modelo 0.21 vs mercado 0.43

## Ultimas 10 fechadas
- YES Will the highest temperature in Lucknow be 31°C on | stop-loss | $-10.11 | 4.7h
- YES Will the highest temperature in Houston be between | take-profit | $+9.68 | 21.3h
- NO Will the Democrats win the Iowa Senate race in 202 | resolvido | $-33.83 | 15.6h
- YES Will the highest temperature in Karachi be 35°C on | stop-loss | $-12.15 | 20.0h
- YES Will the highest temperature in Paris be 10°C on N | stop-loss | $-12.23 | 20.0h
- YES Will the highest temperature in London be 11°C on  | stop-loss | $-12.26 | 20.0h
- YES Will the highest temperature in Hong Kong be 28°C  | take-profit | $+9.50 | 25.3h
- YES Will the highest temperature in Singapore be 32°C  | resolvido | $+17.95 | 33.2h
- YES Will the highest temperature in Tel Aviv be 28°C o | take-profit | $+4.01 | 17.6h
- NO Will the Democrats win the Texas Senate race in 20 | stop-loss | $-35.89 | 40.7h
