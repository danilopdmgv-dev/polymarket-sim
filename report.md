# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-10-30 00:33 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1247.20 (-37.6%) | **Cash:** $1170.79 | **Abertas:** 6 | **Ciclos:** 46
**Fechadas:** 73 | **Win rate:** 22% | **PnL realizado:** $-749.91
**Chamadas ao LLM hoje:** 8

## Por motivo de saida
- resolvido: 1 trades, PnL $-46.54
- stop-loss: 56 trades, PnL $-1101.16
- take-profit: 16 trades, PnL $+397.79

## Por categoria
- Clima: 64 trades, win 19%, PnL $-780.46
- Outros: 1 trades, win 0%, PnL $-18.51
- Politica: 8 trades, win 50%, PnL $+49.05
- **Clima INVERSO (compra o lado oposto ao modelo):** 15 trades, win 27%, PnL $-63.94

## Calibracao do LLM vs mercado (215 mercados resolvidos)
- Brier LLM: 0.2985 | Brier mercado: 0.2168 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (165): LLM 0.3368 vs mercado 0.2279
  - Economia/Dados (5): LLM 0.0318 vs mercado 0.0441
  - Entretenimento (12): LLM 0.2079 vs mercado 0.2153
  - Outros (13): LLM 0.1114 vs mercado 0.1054
  - Politica (20): LLM 0.2253 vs mercado 0.2419
- Fonte clima (165): modelo 0.3368 vs mercado 0.2279 -> PERDENDO
- Fonte llm (50): modelo 0.1722 vs mercado 0.1802 -> GANHANDO
- Clima (146): sigma largo 0.3472 | sigma estreito 0.3180 | mercado 0.2299

## Posicoes abertas
- YES Will the highest temperature in Los Angeles be between 72-73 | entrada 0.50, agora 0.39, LLM 0.19, edge 0.14, medium | Modelo 0.19 vs mercado 0.47
- YES Will the highest temperature in Tel Aviv be 25°C on October  | entrada 0.61, agora 0.56, LLM 0.22, edge 0.17, medium | Modelo 0.22 vs mercado 0.56
- YES Will the highest temperature in Istanbul be 15°C on October  | entrada 0.66, agora 0.71, LLM 0.20, edge 0.24, medium | Modelo 0.20 vs mercado 0.64
- YES Will the highest temperature in Amsterdam be 13°C on October | entrada 0.51, agora 0.51, LLM 0.22, edge 0.11, medium | Modelo 0.22 vs mercado 0.47
- YES Will the highest temperature in Paris be 15°C on October 30? | entrada 0.57, agora 0.57, LLM 0.25, edge 0.14, medium | Modelo 0.25 vs mercado 0.54
- YES Will the highest temperature in Houston be between 78-79°F o | entrada 0.48, agora 0.48, LLM 0.17, edge 0.12, medium | Modelo 0.17 vs mercado 0.43

## Ultimas 10 fechadas
- YES Will the highest temperature in Beijing be 22°C on | stop-loss | $-8.43 | 3.7h
- YES Will the highest temperature in Amsterdam be 14°C  | stop-loss | $-5.85 | 8.2h
- YES Will the highest temperature in Shanghai be 24°C o | stop-loss | $-8.17 | 30.1h
- YES Will the highest temperature in Paris be 16°C on O | stop-loss | $-4.95 | 5.0h
- YES Will the highest temperature in Hong Kong be 29°C  | stop-loss | $-4.24 | 5.0h
- YES Will the highest temperature in New York City be b | take-profit | $+4.93 | 26.3h
- YES Will the highest temperature in Houston be between | take-profit | $+2.61 | 7.6h
- YES Will the highest temperature in Buenos Aires be 25 | stop-loss | $-4.12 | 7.0h
- YES Will the highest temperature in Panama City be 33° | stop-loss | $-11.40 | 7.0h
- YES Will the highest temperature in Amsterdam be 16°C  | take-profit | $+9.67 | 21.3h
