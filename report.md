# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-10-29 02:02 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1300.00 (-35.0%) | **Cash:** $1229.63 | **Abertas:** 5 | **Ciclos:** 41
**Fechadas:** 61 | **Win rate:** 21% | **PnL realizado:** $-701.23
**Chamadas ao LLM hoje:** 6

## Por motivo de saida
- resolvido: 1 trades, PnL $-46.54
- stop-loss: 47 trades, PnL $-1035.27
- take-profit: 13 trades, PnL $+380.58

## Por categoria
- Clima: 52 trades, win 17%, PnL $-731.77
- Outros: 1 trades, win 0%, PnL $-18.51
- Politica: 8 trades, win 50%, PnL $+49.05
- **Clima INVERSO (compra o lado oposto ao modelo):** 3 trades, win 33%, PnL $-15.26

## Calibracao do LLM vs mercado (182 mercados resolvidos)
- Brier LLM: 0.3114 | Brier mercado: 0.2180 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (139): LLM 0.3532 vs mercado 0.2285
  - Economia/Dados (4): LLM 0.0341 vs mercado 0.0431
  - Entretenimento (10): LLM 0.2144 vs mercado 0.2218
  - Outros (9): LLM 0.0881 vs mercado 0.0778
  - Politica (20): LLM 0.2253 vs mercado 0.2419
- Fonte clima (139): modelo 0.3532 vs mercado 0.2285 -> PERDENDO
- Fonte llm (43): modelo 0.1763 vs mercado 0.1844 -> GANHANDO
- Clima (120): sigma largo 0.3685 | sigma estreito 0.3366 | mercado 0.2310

## Posicoes abertas
- YES Will the highest temperature in Wellington be 18°C on Octobe | entrada 0.68, agora 0.86, LLM 0.24, edge 0.23, medium | Modelo 0.24 vs mercado 0.66
- YES Will the highest temperature in Paris be 16°C on October 29? | entrada 0.59, agora 0.55, LLM 0.16, edge 0.19, medium | Modelo 0.16 vs mercado 0.55
- YES Will the highest temperature in New York City be between 68- | entrada 0.66, agora 0.60, LLM 0.23, edge 0.19, medium | Modelo 0.23 vs mercado 0.61
- YES Will the highest temperature in Amsterdam be 16°C on October | entrada 0.57, agora 0.61, LLM 0.22, edge 0.15, medium | Modelo 0.22 vs mercado 0.53
- YES Will the highest temperature in Shanghai be 24°C on October  | entrada 0.55, agora 0.48, LLM 0.10, edge 0.21, medium | Modelo 0.10 vs mercado 0.51

## Ultimas 10 fechadas
- YES Will the highest temperature in Beijing be 21°C on | stop-loss | $-8.36 | 7.6h
- YES Will the highest temperature in Buenos Aires be 23 | stop-loss | $-13.91 | 12.4h
- YES Will the highest temperature in Madrid be 23°C on  | take-profit | $+7.02 | 13.8h
- NO Will the highest temperature in Mexico City be 24° | stop-loss | $-26.92 | 18.2h
- NO Will the highest temperature in Paris be 15°C on O | take-profit | $+21.47 | 18.2h
- NO Will the highest temperature in New York City be b | stop-loss | $-27.04 | 31.7h
- NO Will the highest temperature in Dallas be between  | stop-loss | $-14.39 | 25.7h
- NO Will the highest temperature in Lucknow be 30°C on | stop-loss | $-27.28 | 13.9h
- YES Will Likud win 25-29 seats in the 2026 Israeli leg | take-profit | $+32.22 | 7.8h
- NO Will the highest temperature in Tokyo be 19°C on O | take-profit | $+27.54 | 7.8h
