# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-10-29 08:45 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1279.44 (-36.0%) | **Cash:** $1198.56 | **Abertas:** 6 | **Ciclos:** 42
**Fechadas:** 63 | **Win rate:** 21% | **PnL realizado:** $-719.96
**Chamadas ao LLM hoje:** 14

## Por motivo de saida
- resolvido: 1 trades, PnL $-46.54
- stop-loss: 49 trades, PnL $-1054.00
- take-profit: 13 trades, PnL $+380.58

## Por categoria
- Clima: 54 trades, win 17%, PnL $-750.51
- Outros: 1 trades, win 0%, PnL $-18.51
- Politica: 8 trades, win 50%, PnL $+49.05
- **Clima INVERSO (compra o lado oposto ao modelo):** 5 trades, win 20%, PnL $-33.99

## Calibracao do LLM vs mercado (191 mercados resolvidos)
- Brier LLM: 0.3140 | Brier mercado: 0.2185 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (148): LLM 0.3540 vs mercado 0.2284
  - Economia/Dados (4): LLM 0.0341 vs mercado 0.0431
  - Entretenimento (10): LLM 0.2144 vs mercado 0.2218
  - Outros (9): LLM 0.0881 vs mercado 0.0778
  - Politica (20): LLM 0.2253 vs mercado 0.2419
- Fonte clima (148): modelo 0.3540 vs mercado 0.2284 -> PERDENDO
- Fonte llm (43): modelo 0.1763 vs mercado 0.1844 -> GANHANDO
- Clima (129): sigma largo 0.3683 | sigma estreito 0.3361 | mercado 0.2307

## Posicoes abertas
- YES Will the highest temperature in New York City be between 68- | entrada 0.66, agora 0.67, LLM 0.23, edge 0.19, medium | Modelo 0.23 vs mercado 0.61
- YES Will the highest temperature in Amsterdam be 16°C on October | entrada 0.57, agora 0.63, LLM 0.22, edge 0.15, medium | Modelo 0.22 vs mercado 0.53
- YES Will the highest temperature in Shanghai be 24°C on October  | entrada 0.55, agora 0.45, LLM 0.10, edge 0.21, medium | Modelo 0.10 vs mercado 0.51
- YES Will the highest temperature in Panama City be 33°C on Octob | entrada 0.46, agora 0.46, LLM 0.19, edge 0.13, medium | Modelo 0.19 vs mercado 0.44
- YES Will the highest temperature in Houston be between 82-83°F o | entrada 0.49, agora 0.49, LLM 0.21, edge 0.12, medium | Modelo 0.21 vs mercado 0.46
- YES Will the highest temperature in Buenos Aires be 25°C on Octo | entrada 0.52, agora 0.52, LLM 0.10, edge 0.19, medium | Modelo 0.10 vs mercado 0.48

## Ultimas 10 fechadas
- YES Will the highest temperature in Paris be 16°C on O | stop-loss | $-4.71 | 14.3h
- YES Will the highest temperature in Wellington be 18°C | stop-loss | $-14.03 | 20.3h
- YES Will the highest temperature in Beijing be 21°C on | stop-loss | $-8.36 | 7.6h
- YES Will the highest temperature in Buenos Aires be 23 | stop-loss | $-13.91 | 12.4h
- YES Will the highest temperature in Madrid be 23°C on  | take-profit | $+7.02 | 13.8h
- NO Will the highest temperature in Mexico City be 24° | stop-loss | $-26.92 | 18.2h
- NO Will the highest temperature in Paris be 15°C on O | take-profit | $+21.47 | 18.2h
- NO Will the highest temperature in New York City be b | stop-loss | $-27.04 | 31.7h
- NO Will the highest temperature in Dallas be between  | stop-loss | $-14.39 | 25.7h
- NO Will the highest temperature in Lucknow be 30°C on | stop-loss | $-27.28 | 13.9h
