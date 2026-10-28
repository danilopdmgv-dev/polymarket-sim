# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-10-28 22:46 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1301.72 (-34.9%) | **Cash:** $1224.27 | **Abertas:** 6 | **Ciclos:** 40
**Fechadas:** 60 | **Win rate:** 22% | **PnL realizado:** $-692.87
**Chamadas ao LLM hoje:** 33

## Por motivo de saida
- resolvido: 1 trades, PnL $-46.54
- stop-loss: 46 trades, PnL $-1026.90
- take-profit: 13 trades, PnL $+380.58

## Por categoria
- Clima: 51 trades, win 18%, PnL $-723.41
- Outros: 1 trades, win 0%, PnL $-18.51
- Politica: 8 trades, win 50%, PnL $+49.05
- **Clima INVERSO (compra o lado oposto ao modelo):** 2 trades, win 50%, PnL $-6.89

## Calibracao do LLM vs mercado (180 mercados resolvidos)
- Brier LLM: 0.3119 | Brier mercado: 0.2187 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (137): LLM 0.3544 vs mercado 0.2295
  - Economia/Dados (4): LLM 0.0341 vs mercado 0.0431
  - Entretenimento (10): LLM 0.2144 vs mercado 0.2218
  - Outros (9): LLM 0.0881 vs mercado 0.0778
  - Politica (20): LLM 0.2253 vs mercado 0.2419
- Fonte clima (137): modelo 0.3544 vs mercado 0.2295 -> PERDENDO
- Fonte llm (43): modelo 0.1763 vs mercado 0.1844 -> GANHANDO
- Clima (118): sigma largo 0.3701 | sigma estreito 0.3396 | mercado 0.2322

## Posicoes abertas
- YES Will the highest temperature in Wellington be 18°C on Octobe | entrada 0.68, agora 0.67, LLM 0.24, edge 0.23, medium | Modelo 0.24 vs mercado 0.66
- YES Will the highest temperature in Paris be 16°C on October 29? | entrada 0.59, agora 0.55, LLM 0.16, edge 0.19, medium | Modelo 0.16 vs mercado 0.55
- YES Will the highest temperature in New York City be between 68- | entrada 0.66, agora 0.62, LLM 0.23, edge 0.19, medium | Modelo 0.23 vs mercado 0.61
- YES Will the highest temperature in Amsterdam be 16°C on October | entrada 0.57, agora 0.58, LLM 0.22, edge 0.15, medium | Modelo 0.22 vs mercado 0.53
- YES Will the highest temperature in Shanghai be 24°C on October  | entrada 0.55, agora 0.44, LLM 0.10, edge 0.21, medium | Modelo 0.10 vs mercado 0.51
- YES Will the highest temperature in Beijing be 21°C on October 2 | entrada 0.48, agora 0.43, LLM 0.11, edge 0.17, medium | Modelo 0.11 vs mercado 0.45

## Ultimas 10 fechadas
- YES Will the highest temperature in Buenos Aires be 23 | stop-loss | $-13.91 | 12.4h
- YES Will the highest temperature in Madrid be 23°C on  | take-profit | $+7.02 | 13.8h
- NO Will the highest temperature in Mexico City be 24° | stop-loss | $-26.92 | 18.2h
- NO Will the highest temperature in Paris be 15°C on O | take-profit | $+21.47 | 18.2h
- NO Will the highest temperature in New York City be b | stop-loss | $-27.04 | 31.7h
- NO Will the highest temperature in Dallas be between  | stop-loss | $-14.39 | 25.7h
- NO Will the highest temperature in Lucknow be 30°C on | stop-loss | $-27.28 | 13.9h
- YES Will Likud win 25-29 seats in the 2026 Israeli leg | take-profit | $+32.22 | 7.8h
- NO Will the highest temperature in Tokyo be 19°C on O | take-profit | $+27.54 | 7.8h
- NO Will Yashar win the most seats in the 2026 Israeli | take-profit | $+9.05 | 3.3h
