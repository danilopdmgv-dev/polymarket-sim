# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-10-29 15:51 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1275.16 (-36.2%) | **Cash:** $1193.13 | **Abertas:** 6 | **Ciclos:** 43
**Fechadas:** 66 | **Win rate:** 21% | **PnL realizado:** $-725.81
**Chamadas ao LLM hoje:** 21

## Por motivo de saida
- resolvido: 1 trades, PnL $-46.54
- stop-loss: 51 trades, PnL $-1069.52
- take-profit: 14 trades, PnL $+390.24

## Por categoria
- Clima: 57 trades, win 18%, PnL $-756.36
- Outros: 1 trades, win 0%, PnL $-18.51
- Politica: 8 trades, win 50%, PnL $+49.05
- **Clima INVERSO (compra o lado oposto ao modelo):** 8 trades, win 25%, PnL $-39.84

## Calibracao do LLM vs mercado (200 mercados resolvidos)
- Brier LLM: 0.3048 | Brier mercado: 0.2168 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (156): LLM 0.3421 vs mercado 0.2269
  - Economia/Dados (5): LLM 0.0318 vs mercado 0.0441
  - Entretenimento (10): LLM 0.2144 vs mercado 0.2218
  - Outros (9): LLM 0.0881 vs mercado 0.0778
  - Politica (20): LLM 0.2253 vs mercado 0.2419
- Fonte clima (156): modelo 0.3421 vs mercado 0.2269 -> PERDENDO
- Fonte llm (44): modelo 0.1728 vs mercado 0.1813 -> GANHANDO
- Clima (137): sigma largo 0.3539 | sigma estreito 0.3248 | mercado 0.2288

## Posicoes abertas
- YES Will the highest temperature in New York City be between 68- | entrada 0.66, agora 0.67, LLM 0.23, edge 0.19, medium | Modelo 0.23 vs mercado 0.61
- YES Will the highest temperature in Shanghai be 24°C on October  | entrada 0.55, agora 0.46, LLM 0.10, edge 0.21, medium | Modelo 0.10 vs mercado 0.51
- YES Will the highest temperature in Houston be between 82-83°F o | entrada 0.49, agora 0.59, LLM 0.21, edge 0.12, medium | Modelo 0.21 vs mercado 0.46
- YES Will the highest temperature in Hong Kong be 29°C on October | entrada 0.55, agora 0.55, LLM 0.15, edge 0.19, medium | Modelo 0.15 vs mercado 0.52
- YES Will the highest temperature in Paris be 16°C on October 30? | entrada 0.53, agora 0.53, LLM 0.15, edge 0.20, medium | Modelo 0.15 vs mercado 0.51
- YES Will the highest temperature in Los Angeles be between 72-73 | entrada 0.50, agora 0.50, LLM 0.19, edge 0.14, medium | Modelo 0.19 vs mercado 0.47

## Ultimas 10 fechadas
- YES Will the highest temperature in Buenos Aires be 25 | stop-loss | $-4.12 | 7.0h
- YES Will the highest temperature in Panama City be 33° | stop-loss | $-11.40 | 7.0h
- YES Will the highest temperature in Amsterdam be 16°C  | take-profit | $+9.67 | 21.3h
- YES Will the highest temperature in Paris be 16°C on O | stop-loss | $-4.71 | 14.3h
- YES Will the highest temperature in Wellington be 18°C | stop-loss | $-14.03 | 20.3h
- YES Will the highest temperature in Beijing be 21°C on | stop-loss | $-8.36 | 7.6h
- YES Will the highest temperature in Buenos Aires be 23 | stop-loss | $-13.91 | 12.4h
- YES Will the highest temperature in Madrid be 23°C on  | take-profit | $+7.02 | 13.8h
- NO Will the highest temperature in Mexico City be 24° | stop-loss | $-26.92 | 18.2h
- NO Will the highest temperature in Paris be 15°C on O | take-profit | $+21.47 | 18.2h
