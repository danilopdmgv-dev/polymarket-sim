# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-10-29 20:48 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1267.64 (-36.6%) | **Cash:** $1192.13 | **Abertas:** 6 | **Ciclos:** 45
**Fechadas:** 70 | **Win rate:** 23% | **PnL realizado:** $-727.46
**Chamadas ao LLM hoje:** 37

## Por motivo de saida
- resolvido: 1 trades, PnL $-46.54
- stop-loss: 53 trades, PnL $-1078.71
- take-profit: 16 trades, PnL $+397.79

## Por categoria
- Clima: 61 trades, win 20%, PnL $-758.01
- Outros: 1 trades, win 0%, PnL $-18.51
- Politica: 8 trades, win 50%, PnL $+49.05
- **Clima INVERSO (compra o lado oposto ao modelo):** 12 trades, win 33%, PnL $-41.49

## Calibracao do LLM vs mercado (210 mercados resolvidos)
- Brier LLM: 0.2988 | Brier mercado: 0.2159 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (160): LLM 0.3384 vs mercado 0.2270
  - Economia/Dados (5): LLM 0.0318 vs mercado 0.0441
  - Entretenimento (12): LLM 0.2079 vs mercado 0.2153
  - Outros (13): LLM 0.1114 vs mercado 0.1054
  - Politica (20): LLM 0.2253 vs mercado 0.2419
- Fonte clima (160): modelo 0.3384 vs mercado 0.2270 -> PERDENDO
- Fonte llm (50): modelo 0.1722 vs mercado 0.1802 -> GANHANDO
- Clima (141): sigma largo 0.3494 | sigma estreito 0.3211 | mercado 0.2290

## Posicoes abertas
- YES Will the highest temperature in Shanghai be 24°C on October  | entrada 0.55, agora 0.41, LLM 0.10, edge 0.21, medium | Modelo 0.10 vs mercado 0.51
- YES Will the highest temperature in Los Angeles be between 72-73 | entrada 0.50, agora 0.52, LLM 0.19, edge 0.14, medium | Modelo 0.19 vs mercado 0.47
- YES Will the highest temperature in Amsterdam be 14°C on October | entrada 0.42, agora 0.35, LLM 0.19, edge 0.09, medium | Modelo 0.19 vs mercado 0.39
- YES Will the highest temperature in Tel Aviv be 25°C on October  | entrada 0.61, agora 0.61, LLM 0.22, edge 0.17, medium | Modelo 0.22 vs mercado 0.56
- YES Will the highest temperature in Beijing be 22°C on October 3 | entrada 0.62, agora 0.62, LLM 0.10, edge 0.25, medium | Modelo 0.10 vs mercado 0.57
- YES Will the highest temperature in Istanbul be 15°C on October  | entrada 0.66, agora 0.66, LLM 0.20, edge 0.24, medium | Modelo 0.20 vs mercado 0.64

## Ultimas 10 fechadas
- YES Will the highest temperature in Paris be 16°C on O | stop-loss | $-4.95 | 5.0h
- YES Will the highest temperature in Hong Kong be 29°C  | stop-loss | $-4.24 | 5.0h
- YES Will the highest temperature in New York City be b | take-profit | $+4.93 | 26.3h
- YES Will the highest temperature in Houston be between | take-profit | $+2.61 | 7.6h
- YES Will the highest temperature in Buenos Aires be 25 | stop-loss | $-4.12 | 7.0h
- YES Will the highest temperature in Panama City be 33° | stop-loss | $-11.40 | 7.0h
- YES Will the highest temperature in Amsterdam be 16°C  | take-profit | $+9.67 | 21.3h
- YES Will the highest temperature in Paris be 16°C on O | stop-loss | $-4.71 | 14.3h
- YES Will the highest temperature in Wellington be 18°C | stop-loss | $-14.03 | 20.3h
- YES Will the highest temperature in Beijing be 21°C on | stop-loss | $-8.36 | 7.6h
