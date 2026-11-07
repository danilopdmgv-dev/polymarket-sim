# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-11-07 07:39 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1004.33 (-49.8%) | **Cash:** $943.38 | **Abertas:** 6 | **Ciclos:** 79
**Fechadas:** 156 | **Win rate:** 30% | **PnL realizado:** $-992.85
**Chamadas ao LLM hoje:** 15

## Por motivo de saida
- resolvido: 3 trades, PnL $-62.42
- stop-loss: 107 trades, PnL $-1636.17
- take-profit: 46 trades, PnL $+705.74

## Por categoria
- Clima: 138 trades, win 30%, PnL $-857.16
- Outros: 2 trades, win 50%, PnL $+4.14
- Politica: 16 trades, win 31%, PnL $-139.83
- **Clima INVERSO (compra o lado oposto ao modelo):** 89 trades, win 37%, PnL $-140.64

## Calibracao do LLM vs mercado (580 mercados resolvidos)
- Brier LLM: 0.2952 | Brier mercado: 0.2191 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (429): LLM 0.3339 vs mercado 0.2354
  - Economia/Dados (8): LLM 0.1715 vs mercado 0.1703
  - Entretenimento (31): LLM 0.1449 vs mercado 0.1494
  - Outros (50): LLM 0.1761 vs mercado 0.1774
  - Politica (62): LLM 0.2142 vs mercado 0.1807
- Fonte clima (429): modelo 0.3339 vs mercado 0.2354 -> PERDENDO
- Fonte llm (151): modelo 0.1851 vs mercado 0.1726 -> PERDENDO
- Clima (410): sigma largo 0.3375 | sigma estreito 0.3128 | mercado 0.2365

## Posicoes abertas
- YES Will the highest temperature in Chicago be between 52-53°F o | entrada 0.36, agora 0.31, LLM 0.13, edge 0.10, medium | Modelo 0.13 vs mercado 0.34
- YES Will the highest temperature in Madrid be 19°C on November 7 | entrada 0.59, agora 0.56, LLM 0.19, edge 0.21, medium | Modelo 0.19 vs mercado 0.57
- YES Will the highest temperature in Atlanta be between 66-67°F o | entrada 0.56, agora 0.52, LLM 0.23, edge 0.16, medium | Modelo 0.23 vs mercado 0.54
- YES Will the highest temperature in New York City be between 62- | entrada 0.36, agora 0.36, LLM 0.16, edge 0.09, medium | Modelo 0.16 vs mercado 0.34
- YES Will the highest temperature in Chongqing be 17°C on Novembe | entrada 0.38, agora 0.38, LLM 0.22, edge 0.06, medium | Modelo 0.22 vs mercado 0.36
- YES Will the highest temperature in Amsterdam be 10°C on Novembe | entrada 0.53, agora 0.53, LLM 0.22, edge 0.15, medium | Modelo 0.22 vs mercado 0.51

## Ultimas 10 fechadas
- YES Will the highest temperature in New York City be b | stop-loss | $-10.61 | 9.9h
- YES Will the highest temperature in Tokyo be 20°C on N | take-profit | $+7.75 | 23.5h
- YES Will the highest temperature in Hong Kong be 28°C  | stop-loss | $-10.83 | 23.5h
- YES Will the highest temperature in Houston be between | stop-loss | $-5.03 | 3.8h
- YES Will the highest temperature in Atlanta be between | stop-loss | $-9.05 | 9.4h
- YES Will the highest temperature in Busan be 14°C on N | stop-loss | $-3.47 | 17.3h
- NO Israel x Iran ceasefire continues through November | stop-loss | $-26.54 | 5.6h
- YES Will the highest temperature in Chicago be between | stop-loss | $-5.84 | 5.6h
- YES Will the highest temperature in Atlanta be between | take-profit | $+12.45 | 25.3h
- YES Will the highest temperature in Miami be between 8 | stop-loss | $-4.98 | 27.2h
