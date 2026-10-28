# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-10-28 00:12 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1340.72 (-33.0%) | **Cash:** $1040.55 | **Abertas:** 7 | **Ciclos:** 33
**Fechadas:** 51 | **Win rate:** 18% | **PnL realizado:** $-671.58
**Chamadas ao LLM hoje:** 9

## Por motivo de saida
- resolvido: 1 trades, PnL $-46.54
- stop-loss: 41 trades, PnL $-917.36
- take-profit: 9 trades, PnL $+292.32

## Por categoria
- Clima: 43 trades, win 14%, PnL $-669.90
- Outros: 1 trades, win 0%, PnL $-18.51
- Politica: 7 trades, win 43%, PnL $+16.83

## Calibracao do LLM vs mercado (164 mercados resolvidos)
- Brier LLM: 0.3079 | Brier mercado: 0.2186 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (121): LLM 0.3547 vs mercado 0.2308
  - Economia/Dados (4): LLM 0.0341 vs mercado 0.0431
  - Entretenimento (10): LLM 0.2144 vs mercado 0.2218
  - Outros (9): LLM 0.0881 vs mercado 0.0778
  - Politica (20): LLM 0.2253 vs mercado 0.2419
- Fonte clima (121): modelo 0.3547 vs mercado 0.2308 -> PERDENDO
- Fonte llm (43): modelo 0.1763 vs mercado 0.1844 -> GANHANDO
- Clima (102): sigma largo 0.3729 | sigma estreito 0.3356 | mercado 0.2342

## Posicoes abertas
- NO Will the highest temperature in New York City be between 60- | entrada 0.59, agora 0.49, LLM 0.25, edge 0.08, medium | Modelo 0.25 vs mercado 0.46
- NO Will the highest temperature in Dallas be between 82-83°F on | entrada 0.61, agora 0.71, LLM 0.24, edge 0.08, medium | Modelo 0.24 vs mercado 0.42
- NO Will the highest temperature in Lucknow be 30°C on October 2 | entrada 0.55, agora 0.63, LLM 0.16, edge 0.16, medium | Modelo 0.16 vs mercado 0.48
- NO Will the highest temperature in Tokyo be 19°C on October 28? | entrada 0.58, agora 0.61, LLM 0.28, edge 0.08, medium | Modelo 0.28 vs mercado 0.45
- YES Will Likud win 25-29 seats in the 2026 Israeli legislative e | entrada 0.57, agora 0.62, LLM 0.72, edge 0.06, high | O mercado subestima a concordancia das pesquisas de boca de urna em apontar o Likud firmemente dentr
- NO Will the highest temperature in Paris be 15°C on October 28? | entrada 0.63, agora 0.63, LLM 0.23, edge 0.07, medium | Modelo 0.23 vs mercado 0.41
- NO Will the highest temperature in Mexico City be 24°C on Octob | entrada 0.55, agora 0.55, LLM 0.21, edge 0.13, medium | Modelo 0.21 vs mercado 0.47

## Ultimas 10 fechadas
- NO Will Yashar win the most seats in the 2026 Israeli | take-profit | $+9.05 | 3.3h
- NO Will the highest temperature in Shanghai be 21°C o | stop-loss | $-15.17 | 13.4h
- NO Will the highest temperature in Wellington be 17°C | stop-loss | $-40.81 | 24.0h
- NO Will Yashar win the most seats in the 2026 Israeli | take-profit | $+106.02 | 4.7h
- NO Will the highest temperature in Toronto be 9°C on  | take-profit | $+25.44 | 20.7h
- NO Will the highest temperature in Miami be between 8 | stop-loss | $-41.95 | 16.0h
- NO Will Yashar win the most seats in the 2026 Israeli | stop-loss | $-13.67 | 19.5h
- NO Will the highest temperature in Munich be 17°C on  | stop-loss | $-25.55 | 5.4h
- NO Will the highest temperature in Houston be between | stop-loss | $-14.18 | 10.6h
- NO Will the highest temperature in Dallas be between  | stop-loss | $-15.65 | 19.4h
