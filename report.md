# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-10-31 01:58 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1274.23 (-36.3%) | **Cash:** $1195.54 | **Abertas:** 6 | **Ciclos:** 51
**Fechadas:** 82 | **Win rate:** 26% | **PnL realizado:** $-725.00
**Chamadas ao LLM hoje:** 6

## Por motivo de saida
- resolvido: 1 trades, PnL $-46.54
- stop-loss: 60 trades, PnL $-1135.76
- take-profit: 21 trades, PnL $+457.30

## Por categoria
- Clima: 72 trades, win 22%, PnL $-778.19
- Outros: 2 trades, win 50%, PnL $+4.14
- Politica: 8 trades, win 50%, PnL $+49.05
- **Clima INVERSO (compra o lado oposto ao modelo):** 23 trades, win 35%, PnL $-61.68

## Calibracao do LLM vs mercado (253 mercados resolvidos)
- Brier LLM: 0.3003 | Brier mercado: 0.2166 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (193): LLM 0.3406 vs mercado 0.2293
  - Economia/Dados (6): LLM 0.0559 vs mercado 0.0628
  - Entretenimento (12): LLM 0.2079 vs mercado 0.2153
  - Outros (21): LLM 0.1351 vs mercado 0.1292
  - Politica (21): LLM 0.2169 vs mercado 0.2313
- Fonte clima (193): modelo 0.3406 vs mercado 0.2293 -> PERDENDO
- Fonte llm (60): modelo 0.1704 vs mercado 0.1755 -> GANHANDO
- Clima (174): sigma largo 0.3498 | sigma estreito 0.3250 | mercado 0.2312

## Posicoes abertas
- YES Will the highest temperature in Shenzhen be 30°C on October  | entrada 0.62, agora 0.51, LLM 0.20, edge 0.21, medium | Modelo 0.20 vs mercado 0.59
- YES Will the highest temperature in Tokyo be 23°C on October 31? | entrada 0.45, agora 0.48, LLM 0.22, edge 0.10, medium | Modelo 0.22 vs mercado 0.42
- YES Will the highest temperature in Singapore be 33°C on October | entrada 0.47, agora 0.52, LLM 0.14, edge 0.15, medium | Modelo 0.14 vs mercado 0.44
- YES Will the highest temperature in Buenos Aires be 26°C on Octo | entrada 0.40, agora 0.37, LLM 0.05, edge 0.14, medium | Modelo 0.05 vs mercado 0.35
- YES Will the highest temperature in Milan be 17°C on October 31? | entrada 0.58, agora 0.58, LLM 0.29, edge 0.12, medium | Modelo 0.29 vs mercado 0.54
- YES Will the highest temperature in Paris be 15°C on October 31? | entrada 0.55, agora 0.55, LLM 0.24, edge 0.16, medium | Modelo 0.24 vs mercado 0.54

## Ultimas 10 fechadas
- YES Will the highest temperature in Tel Aviv be 27°C o | stop-loss | $-5.62 | 7.0h
- YES Will the highest temperature in Wellington be 14°C | stop-loss | $-10.79 | 12.2h
- YES Will the highest temperature in Houston be between | take-profit | $+13.53 | 22.2h
- YES Will Vivek Ramaswamy pull the Amy Acton mother ad? | take-profit | $+22.65 | 12.2h
- YES Will the highest temperature in Istanbul be 15°C o | take-profit | $+5.98 | 22.2h
- YES Will the highest temperature in Paris be 15°C on O | stop-loss | $-12.86 | 13.2h
- YES Will the highest temperature in Amsterdam be 13°C  | take-profit | $+11.30 | 13.2h
- YES Will the highest temperature in Tel Aviv be 25°C o | take-profit | $+6.06 | 17.0h
- YES Will the highest temperature in Los Angeles be bet | stop-loss | $-5.32 | 22.0h
- YES Will the highest temperature in Beijing be 22°C on | stop-loss | $-8.43 | 3.7h
