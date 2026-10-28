# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-10-28 12:27 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1355.76 (-32.2%) | **Cash:** $1184.33 | **Abertas:** 6 | **Ciclos:** 38
**Fechadas:** 55 | **Win rate:** 20% | **PnL realizado:** $-653.49
**Chamadas ao LLM hoje:** 25

## Por motivo de saida
- resolvido: 1 trades, PnL $-46.54
- stop-loss: 43 trades, PnL $-959.03
- take-profit: 11 trades, PnL $+352.08

## Por categoria
- Clima: 46 trades, win 15%, PnL $-684.03
- Outros: 1 trades, win 0%, PnL $-18.51
- Politica: 8 trades, win 50%, PnL $+49.05

## Calibracao do LLM vs mercado (172 mercados resolvidos)
- Brier LLM: 0.3135 | Brier mercado: 0.2186 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (129): LLM 0.3593 vs mercado 0.2301
  - Economia/Dados (4): LLM 0.0341 vs mercado 0.0431
  - Entretenimento (10): LLM 0.2144 vs mercado 0.2218
  - Outros (9): LLM 0.0881 vs mercado 0.0778
  - Politica (20): LLM 0.2253 vs mercado 0.2419
- Fonte clima (129): modelo 0.3593 vs mercado 0.2301 -> PERDENDO
- Fonte llm (43): modelo 0.1763 vs mercado 0.1844 -> GANHANDO
- Clima (110): sigma largo 0.3770 | sigma estreito 0.3422 | mercado 0.2331

## Posicoes abertas
- NO Will the highest temperature in New York City be between 60- | entrada 0.59, agora 0.58, LLM 0.25, edge 0.08, medium | Modelo 0.25 vs mercado 0.46
- NO Will the highest temperature in Paris be 15°C on October 28? | entrada 0.63, agora 0.77, LLM 0.23, edge 0.07, medium | Modelo 0.23 vs mercado 0.41
- NO Will the highest temperature in Mexico City be 24°C on Octob | entrada 0.55, agora 0.53, LLM 0.21, edge 0.13, medium | Modelo 0.21 vs mercado 0.47
- YES Will the highest temperature in Madrid be 23°C on October 28 | entrada 0.65, agora 0.70, LLM 0.17, edge 0.26, medium | Modelo 0.17 vs mercado 0.63
- YES Will the highest temperature in Buenos Aires be 23°C on Octo | entrada 0.46, agora 0.50, LLM 0.09, edge 0.18, medium | Modelo 0.09 vs mercado 0.43
- YES Will the highest temperature in Wellington be 18°C on Octobe | entrada 0.68, agora 0.68, LLM 0.24, edge 0.23, medium | Modelo 0.24 vs mercado 0.66

## Ultimas 10 fechadas
- NO Will the highest temperature in Dallas be between  | stop-loss | $-14.39 | 25.7h
- NO Will the highest temperature in Lucknow be 30°C on | stop-loss | $-27.28 | 13.9h
- YES Will Likud win 25-29 seats in the 2026 Israeli leg | take-profit | $+32.22 | 7.8h
- NO Will the highest temperature in Tokyo be 19°C on O | take-profit | $+27.54 | 7.8h
- NO Will Yashar win the most seats in the 2026 Israeli | take-profit | $+9.05 | 3.3h
- NO Will the highest temperature in Shanghai be 21°C o | stop-loss | $-15.17 | 13.4h
- NO Will the highest temperature in Wellington be 17°C | stop-loss | $-40.81 | 24.0h
- NO Will Yashar win the most seats in the 2026 Israeli | take-profit | $+106.02 | 4.7h
- NO Will the highest temperature in Toronto be 9°C on  | take-profit | $+25.44 | 20.7h
- NO Will the highest temperature in Miami be between 8 | stop-loss | $-41.95 | 16.0h
