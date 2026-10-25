# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-10-25 23:52 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1655.29 (-17.2%) | **Cash:** $1358.94 | **Abertas:** 6 | **Ciclos:** 23
**Fechadas:** 26 | **Win rate:** 15% | **PnL realizado:** $-346.67
**Chamadas ao LLM hoje:** 60

## Por motivo de saida
- stop-loss: 22 trades, PnL $-424.19
- take-profit: 4 trades, PnL $+77.51

## Por categoria
- Clima: 22 trades, win 14%, PnL $-290.13
- Outros: 1 trades, win 0%, PnL $-18.51
- Politica: 3 trades, win 33%, PnL $-38.04

## Calibracao do LLM vs mercado (77 mercados resolvidos)
- Brier LLM: 0.2764 | Brier mercado: 0.2052 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (56): LLM 0.3353 vs mercado 0.2409
  - Economia/Dados (4): LLM 0.0341 vs mercado 0.0431
  - Entretenimento (5): LLM 0.3056 vs mercado 0.3154
  - Outros (8): LLM 0.0760 vs mercado 0.0650
  - Politica (4): LLM 0.0583 vs mercado 0.0102
- Fonte clima (56): modelo 0.3353 vs mercado 0.2409 -> PERDENDO
- Fonte llm (21): modelo 0.1193 vs mercado 0.1100 -> PERDENDO
- Clima (37): sigma largo 0.3756 | sigma estreito 0.3407 | mercado 0.2555

## Posicoes abertas
- NO Will the highest temperature in Dallas be between 80-81°F on | entrada 0.49, agora 0.57, LLM 0.25, edge 0.15, medium | Modelo 0.25 vs mercado 0.54
- NO Will the highest temperature in Paris be 15°C on October 26? | entrada 0.60, agora 0.53, LLM 0.14, edge 0.15, medium | Modelo 0.14 vs mercado 0.42
- NO Will the highest temperature in Beijing be 19°C on October 2 | entrada 0.54, agora 0.61, LLM 0.19, edge 0.15, medium | Modelo 0.19 vs mercado 0.50
- NO Will the highest temperature in Chengdu be 20°C on October 2 | entrada 0.35, agora 0.30, LLM 0.24, edge 0.22, medium | Modelo 0.24 vs mercado 0.70
- NO Will the highest temperature in Houston be between 80-81°F o | entrada 0.60, agora 0.60, LLM 0.20, edge 0.10, medium | Modelo 0.20 vs mercado 0.45
- NO Will the highest temperature in Milan be 16°C on October 26? | entrada 0.53, agora 0.53, LLM 0.27, edge 0.11, medium | Modelo 0.27 vs mercado 0.50

## Ultimas 10 fechadas
- NO Will the highest temperature in Wellington be 17°C | take-profit | $+32.10 | 7.2h
- NO Will the highest temperature in Amsterdam be 14°C  | take-profit | $+13.51 | 7.2h
- NO Will the highest temperature in London be 17°C on  | stop-loss | $-5.39 | 22.5h
- NO Will Flávio Bolsonaro win the second round of the  | take-profit | $+7.10 | 28.2h
- NO Will the highest temperature in Dallas be between  | stop-loss | $-5.76 | 22.4h
- NO Will the highest temperature in Toronto be 18°C on | stop-loss | $-9.33 | 22.4h
- NO Will the highest temperature in Helsinki be 12°C o | stop-loss | $-7.94 | 33.9h
- NO Will the highest temperature in Atlanta be between | stop-loss | $-16.45 | 48.4h
- NO Will the highest temperature in London be 14°C on  | stop-loss | $-49.10 | 5.7h
- NO Will the highest temperature in New York City be b | stop-loss | $-5.42 | 7.1h
