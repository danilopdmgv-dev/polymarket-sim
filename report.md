# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-10-29 16:24 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1272.20 (-36.4%) | **Cash:** $1195.82 | **Abertas:** 6 | **Ciclos:** 44
**Fechadas:** 67 | **Win rate:** 22% | **PnL realizado:** $-723.20
**Chamadas ao LLM hoje:** 29

## Por motivo de saida
- resolvido: 1 trades, PnL $-46.54
- stop-loss: 51 trades, PnL $-1069.52
- take-profit: 15 trades, PnL $+392.85

## Por categoria
- Clima: 58 trades, win 19%, PnL $-753.75
- Outros: 1 trades, win 0%, PnL $-18.51
- Politica: 8 trades, win 50%, PnL $+49.05
- **Clima INVERSO (compra o lado oposto ao modelo):** 9 trades, win 33%, PnL $-37.23

## Calibracao do LLM vs mercado (206 mercados resolvidos)
- Brier LLM: 0.3008 | Brier mercado: 0.2155 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (156): LLM 0.3421 vs mercado 0.2269
  - Economia/Dados (5): LLM 0.0318 vs mercado 0.0441
  - Entretenimento (12): LLM 0.2079 vs mercado 0.2153
  - Outros (13): LLM 0.1114 vs mercado 0.1054
  - Politica (20): LLM 0.2253 vs mercado 0.2419
- Fonte clima (156): modelo 0.3421 vs mercado 0.2269 -> PERDENDO
- Fonte llm (50): modelo 0.1722 vs mercado 0.1802 -> GANHANDO
- Clima (137): sigma largo 0.3539 | sigma estreito 0.3248 | mercado 0.2288

## Posicoes abertas
- YES Will the highest temperature in New York City be between 68- | entrada 0.66, agora 0.63, LLM 0.23, edge 0.19, medium | Modelo 0.23 vs mercado 0.61
- YES Will the highest temperature in Shanghai be 24°C on October  | entrada 0.55, agora 0.49, LLM 0.10, edge 0.21, medium | Modelo 0.10 vs mercado 0.51
- YES Will the highest temperature in Hong Kong be 29°C on October | entrada 0.55, agora 0.50, LLM 0.15, edge 0.19, medium | Modelo 0.15 vs mercado 0.52
- YES Will the highest temperature in Paris be 16°C on October 30? | entrada 0.53, agora 0.50, LLM 0.15, edge 0.20, medium | Modelo 0.15 vs mercado 0.51
- YES Will the highest temperature in Los Angeles be between 72-73 | entrada 0.50, agora 0.47, LLM 0.19, edge 0.14, medium | Modelo 0.19 vs mercado 0.47
- YES Will the highest temperature in Amsterdam be 14°C on October | entrada 0.42, agora 0.42, LLM 0.19, edge 0.09, medium | Modelo 0.19 vs mercado 0.39

## Ultimas 10 fechadas
- YES Will the highest temperature in Houston be between | take-profit | $+2.61 | 7.6h
- YES Will the highest temperature in Buenos Aires be 25 | stop-loss | $-4.12 | 7.0h
- YES Will the highest temperature in Panama City be 33° | stop-loss | $-11.40 | 7.0h
- YES Will the highest temperature in Amsterdam be 16°C  | take-profit | $+9.67 | 21.3h
- YES Will the highest temperature in Paris be 16°C on O | stop-loss | $-4.71 | 14.3h
- YES Will the highest temperature in Wellington be 18°C | stop-loss | $-14.03 | 20.3h
- YES Will the highest temperature in Beijing be 21°C on | stop-loss | $-8.36 | 7.6h
- YES Will the highest temperature in Buenos Aires be 23 | stop-loss | $-13.91 | 12.4h
- YES Will the highest temperature in Madrid be 23°C on  | take-profit | $+7.02 | 13.8h
- NO Will the highest temperature in Mexico City be 24° | stop-loss | $-26.92 | 18.2h
