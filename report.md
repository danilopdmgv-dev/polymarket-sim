# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-10-25 21:59 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1638.75 (-18.1%) | **Cash:** $1315.91 | **Abertas:** 6 | **Ciclos:** 22
**Fechadas:** 24 | **Win rate:** 8% | **PnL realizado:** $-392.29
**Chamadas ao LLM hoje:** 52

## Por motivo de saida
- stop-loss: 22 trades, PnL $-424.19
- take-profit: 2 trades, PnL $+31.90

## Por categoria
- Clima: 20 trades, win 5%, PnL $-335.74
- Outros: 1 trades, win 0%, PnL $-18.51
- Politica: 3 trades, win 33%, PnL $-38.04

## Calibracao do LLM vs mercado (73 mercados resolvidos)
- Brier LLM: 0.2812 | Brier mercado: 0.1979 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (52): LLM 0.3466 vs mercado 0.2334
  - Economia/Dados (4): LLM 0.0341 vs mercado 0.0431
  - Entretenimento (5): LLM 0.3056 vs mercado 0.3154
  - Outros (8): LLM 0.0760 vs mercado 0.0650
  - Politica (4): LLM 0.0583 vs mercado 0.0102
- Fonte clima (52): modelo 0.3466 vs mercado 0.2334 -> PERDENDO
- Fonte llm (21): modelo 0.1193 vs mercado 0.1100 -> PERDENDO
- Clima (33): sigma largo 0.3983 | sigma estreito 0.3592 | mercado 0.2454

## Posicoes abertas
- NO Will the highest temperature in Dallas be between 80-81°F on | entrada 0.49, agora 0.56, LLM 0.25, edge 0.15, medium | Modelo 0.25 vs mercado 0.54
- NO Will the highest temperature in Amsterdam be 14°C on October | entrada 0.50, agora 0.67, LLM 0.18, edge 0.18, medium | Modelo 0.18 vs mercado 0.53
- NO Will the highest temperature in Paris be 15°C on October 26? | entrada 0.60, agora 0.58, LLM 0.14, edge 0.15, medium | Modelo 0.14 vs mercado 0.42
- NO Will the highest temperature in Beijing be 19°C on October 2 | entrada 0.54, agora 0.53, LLM 0.19, edge 0.15, medium | Modelo 0.19 vs mercado 0.50
- NO Will the highest temperature in Wellington be 17°C on Octobe | entrada 0.57, agora 0.68, LLM 0.24, edge 0.10, medium | Modelo 0.24 vs mercado 0.47
- NO Will the highest temperature in Chengdu be 20°C on October 2 | entrada 0.35, agora 0.35, LLM 0.24, edge 0.22, medium | Modelo 0.24 vs mercado 0.70

## Ultimas 10 fechadas
- NO Will the highest temperature in London be 17°C on  | stop-loss | $-5.39 | 22.5h
- NO Will Flávio Bolsonaro win the second round of the  | take-profit | $+7.10 | 28.2h
- NO Will the highest temperature in Dallas be between  | stop-loss | $-5.76 | 22.4h
- NO Will the highest temperature in Toronto be 18°C on | stop-loss | $-9.33 | 22.4h
- NO Will the highest temperature in Helsinki be 12°C o | stop-loss | $-7.94 | 33.9h
- NO Will the highest temperature in Atlanta be between | stop-loss | $-16.45 | 48.4h
- NO Will the highest temperature in London be 14°C on  | stop-loss | $-49.10 | 5.7h
- NO Will the highest temperature in New York City be b | stop-loss | $-5.42 | 7.1h
- NO Will the highest temperature in Amsterdam be 13°C  | stop-loss | $-5.63 | 19.2h
- NO Will the highest temperature in Atlanta be between | take-profit | $+24.80 | 38.7h
