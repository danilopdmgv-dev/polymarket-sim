# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-11-07 01:31 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1020.13 (-49.0%) | **Cash:** $955.72 | **Abertas:** 6 | **Ciclos:** 78
**Fechadas:** 153 | **Win rate:** 30% | **PnL realizado:** $-979.16
**Chamadas ao LLM hoje:** 8

## Por motivo de saida
- resolvido: 3 trades, PnL $-62.42
- stop-loss: 105 trades, PnL $-1614.74
- take-profit: 45 trades, PnL $+697.99

## Por categoria
- Clima: 135 trades, win 30%, PnL $-843.47
- Outros: 2 trades, win 50%, PnL $+4.14
- Politica: 16 trades, win 31%, PnL $-139.83
- **Clima INVERSO (compra o lado oposto ao modelo):** 86 trades, win 37%, PnL $-126.96

## Calibracao do LLM vs mercado (569 mercados resolvidos)
- Brier LLM: 0.2959 | Brier mercado: 0.2186 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (418): LLM 0.3359 vs mercado 0.2352
  - Economia/Dados (8): LLM 0.1715 vs mercado 0.1703
  - Entretenimento (31): LLM 0.1449 vs mercado 0.1494
  - Outros (50): LLM 0.1761 vs mercado 0.1774
  - Politica (62): LLM 0.2142 vs mercado 0.1807
- Fonte clima (418): modelo 0.3359 vs mercado 0.2352 -> PERDENDO
- Fonte llm (151): modelo 0.1851 vs mercado 0.1726 -> PERDENDO
- Clima (399): sigma largo 0.3396 | sigma estreito 0.3147 | mercado 0.2363

## Posicoes abertas
- YES Will the highest temperature in Hong Kong be 28°C on Novembe | entrada 0.47, agora 0.51, LLM 0.20, edge 0.13, medium | Modelo 0.20 vs mercado 0.45
- YES Will the highest temperature in Tokyo be 20°C on November 7? | entrada 0.56, agora 0.49, LLM 0.18, edge 0.18, medium | Modelo 0.18 vs mercado 0.53
- YES Will the highest temperature in New York City be between 60- | entrada 0.44, agora 0.43, LLM 0.26, edge 0.08, medium | Modelo 0.26 vs mercado 0.42
- YES Will the highest temperature in Chicago be between 52-53°F o | entrada 0.36, agora 0.36, LLM 0.13, edge 0.10, medium | Modelo 0.13 vs mercado 0.34
- YES Will the highest temperature in Madrid be 19°C on November 7 | entrada 0.59, agora 0.59, LLM 0.19, edge 0.21, medium | Modelo 0.19 vs mercado 0.57
- YES Will the highest temperature in Atlanta be between 66-67°F o | entrada 0.56, agora 0.56, LLM 0.23, edge 0.16, medium | Modelo 0.23 vs mercado 0.54

## Ultimas 10 fechadas
- YES Will the highest temperature in Houston be between | stop-loss | $-5.03 | 3.8h
- YES Will the highest temperature in Atlanta be between | stop-loss | $-9.05 | 9.4h
- YES Will the highest temperature in Busan be 14°C on N | stop-loss | $-3.47 | 17.3h
- NO Israel x Iran ceasefire continues through November | stop-loss | $-26.54 | 5.6h
- YES Will the highest temperature in Chicago be between | stop-loss | $-5.84 | 5.6h
- YES Will the highest temperature in Atlanta be between | take-profit | $+12.45 | 25.3h
- YES Will the highest temperature in Miami be between 8 | stop-loss | $-4.98 | 27.2h
- YES Will the highest temperature in Milan be 11°C on N | take-profit | $+12.24 | 35.6h
- YES Will the highest temperature in London be 12°C on  | stop-loss | $-4.04 | 4.6h
- YES Will the highest temperature in San Francisco be b | stop-loss | $-3.56 | 4.6h
