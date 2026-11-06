# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-11-06 21:43 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1033.54 (-48.3%) | **Cash:** $972.38 | **Abertas:** 6 | **Ciclos:** 77
**Fechadas:** 150 | **Win rate:** 31% | **PnL realizado:** $-961.62
**Chamadas ao LLM hoje:** 30

## Por motivo de saida
- resolvido: 3 trades, PnL $-62.42
- stop-loss: 102 trades, PnL $-1597.19
- take-profit: 45 trades, PnL $+697.99

## Por categoria
- Clima: 132 trades, win 30%, PnL $-825.93
- Outros: 2 trades, win 50%, PnL $+4.14
- Politica: 16 trades, win 31%, PnL $-139.83
- **Clima INVERSO (compra o lado oposto ao modelo):** 83 trades, win 39%, PnL $-109.42

## Calibracao do LLM vs mercado (561 mercados resolvidos)
- Brier LLM: 0.2970 | Brier mercado: 0.2189 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (412): LLM 0.3368 vs mercado 0.2358
  - Economia/Dados (8): LLM 0.1715 vs mercado 0.1703
  - Entretenimento (31): LLM 0.1449 vs mercado 0.1494
  - Outros (50): LLM 0.1761 vs mercado 0.1774
  - Politica (60): LLM 0.2193 vs mercado 0.1803
- Fonte clima (412): modelo 0.3368 vs mercado 0.2358 -> PERDENDO
- Fonte llm (149): modelo 0.1867 vs mercado 0.1723 -> PERDENDO
- Clima (393): sigma largo 0.3407 | sigma estreito 0.3152 | mercado 0.2369

## Posicoes abertas
- YES Will the highest temperature in Hong Kong be 28°C on Novembe | entrada 0.47, agora 0.42, LLM 0.20, edge 0.13, medium | Modelo 0.20 vs mercado 0.45
- YES Will the highest temperature in Tokyo be 20°C on November 7? | entrada 0.56, agora 0.56, LLM 0.18, edge 0.18, medium | Modelo 0.18 vs mercado 0.53
- YES Will the highest temperature in Busan be 14°C on November 7? | entrada 0.59, agora 0.56, LLM 0.14, edge 0.22, medium | Modelo 0.14 vs mercado 0.56
- YES Will the highest temperature in Atlanta be between 64-65°F o | entrada 0.47, agora 0.34, LLM 0.25, edge 0.09, medium | Modelo 0.25 vs mercado 0.45
- YES Will the highest temperature in New York City be between 60- | entrada 0.44, agora 0.44, LLM 0.26, edge 0.08, medium | Modelo 0.26 vs mercado 0.42
- YES Will the highest temperature in Houston be between 76-77°F o | entrada 0.37, agora 0.37, LLM 0.20, edge 0.07, medium | Modelo 0.20 vs mercado 0.35

## Ultimas 10 fechadas
- NO Israel x Iran ceasefire continues through November | stop-loss | $-26.54 | 5.6h
- YES Will the highest temperature in Chicago be between | stop-loss | $-5.84 | 5.6h
- YES Will the highest temperature in Atlanta be between | take-profit | $+12.45 | 25.3h
- YES Will the highest temperature in Miami be between 8 | stop-loss | $-4.98 | 27.2h
- YES Will the highest temperature in Milan be 11°C on N | take-profit | $+12.24 | 35.6h
- YES Will the highest temperature in London be 12°C on  | stop-loss | $-4.04 | 4.6h
- YES Will the highest temperature in San Francisco be b | stop-loss | $-3.56 | 4.6h
- YES Will the highest temperature in Cape Town be 20°C  | stop-loss | $-4.09 | 12.1h
- YES Will the highest temperature in Busan be 17°C on N | stop-loss | $-8.24 | 7.6h
- YES Will the highest temperature in Amsterdam be 10°C  | stop-loss | $-4.59 | 7.6h
