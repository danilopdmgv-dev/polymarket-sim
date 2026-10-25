# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-10-25 19:26 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1633.70 (-18.3%) | **Cash:** $1352.61 | **Abertas:** 6 | **Ciclos:** 21
**Fechadas:** 23 | **Win rate:** 9% | **PnL realizado:** $-386.90
**Chamadas ao LLM hoje:** 44

## Por motivo de saida
- stop-loss: 21 trades, PnL $-418.80
- take-profit: 2 trades, PnL $+31.90

## Por categoria
- Clima: 19 trades, win 5%, PnL $-330.35
- Outros: 1 trades, win 0%, PnL $-18.51
- Politica: 3 trades, win 33%, PnL $-38.04

## Calibracao do LLM vs mercado (72 mercados resolvidos)
- Brier LLM: 0.2765 | Brier mercado: 0.1964 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (51): LLM 0.3412 vs mercado 0.2319
  - Economia/Dados (4): LLM 0.0341 vs mercado 0.0431
  - Entretenimento (5): LLM 0.3056 vs mercado 0.3154
  - Outros (8): LLM 0.0760 vs mercado 0.0650
  - Politica (4): LLM 0.0583 vs mercado 0.0102
- Fonte clima (51): modelo 0.3412 vs mercado 0.2319 -> PERDENDO
- Fonte llm (21): modelo 0.1193 vs mercado 0.1100 -> PERDENDO
- Clima (32): sigma largo 0.3913 | sigma estreito 0.3549 | mercado 0.2434

## Posicoes abertas
- NO Will the highest temperature in London be 17°C on October 26 | entrada 0.46, agora 0.35, LLM 0.22, edge 0.18, medium | Modelo 0.22 vs mercado 0.57
- NO Will the highest temperature in Dallas be between 80-81°F on | entrada 0.49, agora 0.56, LLM 0.25, edge 0.15, medium | Modelo 0.25 vs mercado 0.54
- NO Will the highest temperature in Amsterdam be 14°C on October | entrada 0.50, agora 0.65, LLM 0.18, edge 0.18, medium | Modelo 0.18 vs mercado 0.53
- NO Will the highest temperature in Paris be 15°C on October 26? | entrada 0.60, agora 0.59, LLM 0.14, edge 0.15, medium | Modelo 0.14 vs mercado 0.42
- NO Will the highest temperature in Beijing be 19°C on October 2 | entrada 0.54, agora 0.52, LLM 0.19, edge 0.15, medium | Modelo 0.19 vs mercado 0.50
- NO Will the highest temperature in Wellington be 17°C on Octobe | entrada 0.57, agora 0.63, LLM 0.24, edge 0.10, medium | Modelo 0.24 vs mercado 0.47

## Ultimas 10 fechadas
- NO Will Flávio Bolsonaro win the second round of the  | take-profit | $+7.10 | 28.2h
- NO Will the highest temperature in Dallas be between  | stop-loss | $-5.76 | 22.4h
- NO Will the highest temperature in Toronto be 18°C on | stop-loss | $-9.33 | 22.4h
- NO Will the highest temperature in Helsinki be 12°C o | stop-loss | $-7.94 | 33.9h
- NO Will the highest temperature in Atlanta be between | stop-loss | $-16.45 | 48.4h
- NO Will the highest temperature in London be 14°C on  | stop-loss | $-49.10 | 5.7h
- NO Will the highest temperature in New York City be b | stop-loss | $-5.42 | 7.1h
- NO Will the highest temperature in Amsterdam be 13°C  | stop-loss | $-5.63 | 19.2h
- NO Will the highest temperature in Atlanta be between | take-profit | $+24.80 | 38.7h
- NO Will the highest temperature in Shanghai be 23°C o | stop-loss | $-7.11 | 3.1h
