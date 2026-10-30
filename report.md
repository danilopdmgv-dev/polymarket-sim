# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-10-30 18:58 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1284.06 (-35.8%) | **Cash:** $1199.08 | **Abertas:** 6 | **Ciclos:** 49
**Fechadas:** 79 | **Win rate:** 25% | **PnL realizado:** $-722.12
**Chamadas ao LLM hoje:** 29

## Por motivo de saida
- resolvido: 1 trades, PnL $-46.54
- stop-loss: 58 trades, PnL $-1119.35
- take-profit: 20 trades, PnL $+443.77

## Por categoria
- Clima: 69 trades, win 22%, PnL $-775.31
- Outros: 2 trades, win 50%, PnL $+4.14
- Politica: 8 trades, win 50%, PnL $+49.05
- **Clima INVERSO (compra o lado oposto ao modelo):** 20 trades, win 35%, PnL $-58.79

## Calibracao do LLM vs mercado (244 mercados resolvidos)
- Brier LLM: 0.2958 | Brier mercado: 0.2156 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (184): LLM 0.3367 vs mercado 0.2287
  - Economia/Dados (6): LLM 0.0559 vs mercado 0.0628
  - Entretenimento (12): LLM 0.2079 vs mercado 0.2153
  - Outros (21): LLM 0.1351 vs mercado 0.1292
  - Politica (21): LLM 0.2169 vs mercado 0.2313
- Fonte clima (184): modelo 0.3367 vs mercado 0.2287 -> PERDENDO
- Fonte llm (60): modelo 0.1704 vs mercado 0.1755 -> GANHANDO
- Clima (165): sigma largo 0.3459 | sigma estreito 0.3187 | mercado 0.2306

## Posicoes abertas
- YES Will the highest temperature in Houston be between 78-79°F o | entrada 0.48, agora 0.70, LLM 0.17, edge 0.12, medium | Modelo 0.17 vs mercado 0.43
- YES Will the highest temperature in Shenzhen be 30°C on October  | entrada 0.62, agora 0.61, LLM 0.20, edge 0.21, medium | Modelo 0.20 vs mercado 0.59
- YES Will the highest temperature in Wellington be 14°C on Octobe | entrada 0.53, agora 0.52, LLM 0.21, edge 0.16, medium | Modelo 0.21 vs mercado 0.51
- YES Will the highest temperature in Tokyo be 23°C on October 31? | entrada 0.45, agora 0.48, LLM 0.22, edge 0.10, medium | Modelo 0.22 vs mercado 0.42
- YES Will the highest temperature in Singapore be 33°C on October | entrada 0.47, agora 0.45, LLM 0.14, edge 0.15, medium | Modelo 0.14 vs mercado 0.44
- YES Will the highest temperature in Tel Aviv be 27°C on October  | entrada 0.41, agora 0.41, LLM 0.20, edge 0.08, medium | Modelo 0.20 vs mercado 0.38

## Ultimas 10 fechadas
- YES Will Vivek Ramaswamy pull the Amy Acton mother ad? | take-profit | $+22.65 | 12.2h
- YES Will the highest temperature in Istanbul be 15°C o | take-profit | $+5.98 | 22.2h
- YES Will the highest temperature in Paris be 15°C on O | stop-loss | $-12.86 | 13.2h
- YES Will the highest temperature in Amsterdam be 13°C  | take-profit | $+11.30 | 13.2h
- YES Will the highest temperature in Tel Aviv be 25°C o | take-profit | $+6.06 | 17.0h
- YES Will the highest temperature in Los Angeles be bet | stop-loss | $-5.32 | 22.0h
- YES Will the highest temperature in Beijing be 22°C on | stop-loss | $-8.43 | 3.7h
- YES Will the highest temperature in Amsterdam be 14°C  | stop-loss | $-5.85 | 8.2h
- YES Will the highest temperature in Shanghai be 24°C o | stop-loss | $-8.17 | 30.1h
- YES Will the highest temperature in Paris be 16°C on O | stop-loss | $-4.95 | 5.0h
