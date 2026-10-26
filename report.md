# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-10-26 08:21 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1545.92 (-22.7%) | **Cash:** $1293.09 | **Abertas:** 5 | **Ciclos:** 25
**Fechadas:** 31 | **Win rate:** 13% | **PnL realizado:** $-466.58
**Chamadas ao LLM hoje:** 16

## Por motivo de saida
- stop-loss: 27 trades, PnL $-544.09
- take-profit: 4 trades, PnL $+77.51

## Por categoria
- Clima: 27 trades, win 11%, PnL $-410.04
- Outros: 1 trades, win 0%, PnL $-18.51
- Politica: 3 trades, win 33%, PnL $-38.04

## Calibracao do LLM vs mercado (103 mercados resolvidos)
- Brier LLM: 0.2911 | Brier mercado: 0.2167 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (72): LLM 0.3383 vs mercado 0.2285
  - Economia/Dados (4): LLM 0.0341 vs mercado 0.0431
  - Entretenimento (5): LLM 0.3056 vs mercado 0.3154
  - Outros (8): LLM 0.0760 vs mercado 0.0650
  - Politica (14): LLM 0.2394 vs mercado 0.2568
- Fonte clima (72): modelo 0.3383 vs mercado 0.2285 -> PERDENDO
- Fonte llm (31): modelo 0.1814 vs mercado 0.1892 -> GANHANDO
- Clima (53): sigma largo 0.3675 | sigma estreito 0.3338 | mercado 0.2342

## Posicoes abertas
- NO Will the highest temperature in Dallas be between 80-81°F on | entrada 0.49, agora 0.61, LLM 0.25, edge 0.15, medium | Modelo 0.25 vs mercado 0.54
- NO Will the highest temperature in Houston be between 80-81°F o | entrada 0.60, agora 0.56, LLM 0.20, edge 0.10, medium | Modelo 0.20 vs mercado 0.45
- NO Will the highest temperature in Toronto be 16°C on October 2 | entrada 0.62, agora 0.66, LLM 0.15, edge 0.13, medium | Modelo 0.15 vs mercado 0.41
- NO Will the highest temperature in New York City be between 70- | entrada 0.48, agora 0.48, LLM 0.32, edge 0.11, medium | Modelo 0.32 vs mercado 0.55
- NO Will the highest temperature in Wellington be 16°C on Octobe | entrada 0.36, agora 0.36, LLM 0.22, edge 0.24, medium | Modelo 0.22 vs mercado 0.68

## Ultimas 10 fechadas
- NO Will the highest temperature in Amsterdam be 13°C  | stop-loss | $-15.06 | 5.8h
- NO Will the highest temperature in Milan be 16°C on O | stop-loss | $-15.86 | 8.5h
- NO Will the highest temperature in Beijing be 19°C on | stop-loss | $-47.47 | 15.7h
- NO Will the highest temperature in Chengdu be 20°C on | stop-loss | $-26.22 | 4.6h
- NO Will the highest temperature in Paris be 15°C on O | stop-loss | $-15.29 | 9.9h
- NO Will the highest temperature in Wellington be 17°C | take-profit | $+32.10 | 7.2h
- NO Will the highest temperature in Amsterdam be 14°C  | take-profit | $+13.51 | 7.2h
- NO Will the highest temperature in London be 17°C on  | stop-loss | $-5.39 | 22.5h
- NO Will Flávio Bolsonaro win the second round of the  | take-profit | $+7.10 | 28.2h
- NO Will the highest temperature in Dallas be between  | stop-loss | $-5.76 | 22.4h
