# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-10-30 13:46 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1243.46 (-37.8%) | **Cash:** $1120.69 | **Abertas:** 7 | **Ciclos:** 48
**Fechadas:** 77 | **Win rate:** 23% | **PnL realizado:** $-750.75
**Chamadas ao LLM hoje:** 22

## Por motivo de saida
- resolvido: 1 trades, PnL $-46.54
- stop-loss: 58 trades, PnL $-1119.35
- take-profit: 18 trades, PnL $+415.14

## Por categoria
- Clima: 68 trades, win 21%, PnL $-781.29
- Outros: 1 trades, win 0%, PnL $-18.51
- Politica: 8 trades, win 50%, PnL $+49.05
- **Clima INVERSO (compra o lado oposto ao modelo):** 19 trades, win 32%, PnL $-64.77

## Calibracao do LLM vs mercado (234 mercados resolvidos)
- Brier LLM: 0.3013 | Brier mercado: 0.2178 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (181): LLM 0.3387 vs mercado 0.2286
  - Economia/Dados (5): LLM 0.0318 vs mercado 0.0441
  - Entretenimento (12): LLM 0.2079 vs mercado 0.2153
  - Outros (15): LLM 0.1333 vs mercado 0.1289
  - Politica (21): LLM 0.2169 vs mercado 0.2313
- Fonte clima (181): modelo 0.3387 vs mercado 0.2286 -> PERDENDO
- Fonte llm (53): modelo 0.1737 vs mercado 0.1810 -> GANHANDO
- Clima (162): sigma largo 0.3483 | sigma estreito 0.3207 | mercado 0.2305

## Posicoes abertas
- YES Will the highest temperature in Istanbul be 15°C on October  | entrada 0.66, agora 0.93, LLM 0.20, edge 0.24, medium | Modelo 0.20 vs mercado 0.64
- YES Will the highest temperature in Houston be between 78-79°F o | entrada 0.48, agora 0.46, LLM 0.17, edge 0.12, medium | Modelo 0.17 vs mercado 0.43
- YES Will Vivek Ramaswamy pull the Amy Acton mother ad? | entrada 0.52, agora 0.41, LLM 0.99, edge 0.22, high | O mercado de 0.50 esta atrasado em relacao aos multiplos, recem-publicados relatorios da midia confi
- YES Will the highest temperature in Shenzhen be 30°C on October  | entrada 0.62, agora 0.62, LLM 0.20, edge 0.21, medium | Modelo 0.20 vs mercado 0.59
- YES Will the highest temperature in Wellington be 14°C on Octobe | entrada 0.53, agora 0.53, LLM 0.21, edge 0.16, medium | Modelo 0.21 vs mercado 0.51
- YES Will the highest temperature in Tokyo be 23°C on October 31? | entrada 0.45, agora 0.45, LLM 0.22, edge 0.10, medium | Modelo 0.22 vs mercado 0.42
- YES Will the highest temperature in Singapore be 33°C on October | entrada 0.47, agora 0.47, LLM 0.14, edge 0.15, medium | Modelo 0.14 vs mercado 0.44

## Ultimas 10 fechadas
- YES Will the highest temperature in Paris be 15°C on O | stop-loss | $-12.86 | 13.2h
- YES Will the highest temperature in Amsterdam be 13°C  | take-profit | $+11.30 | 13.2h
- YES Will the highest temperature in Tel Aviv be 25°C o | take-profit | $+6.06 | 17.0h
- YES Will the highest temperature in Los Angeles be bet | stop-loss | $-5.32 | 22.0h
- YES Will the highest temperature in Beijing be 22°C on | stop-loss | $-8.43 | 3.7h
- YES Will the highest temperature in Amsterdam be 14°C  | stop-loss | $-5.85 | 8.2h
- YES Will the highest temperature in Shanghai be 24°C o | stop-loss | $-8.17 | 30.1h
- YES Will the highest temperature in Paris be 16°C on O | stop-loss | $-4.95 | 5.0h
- YES Will the highest temperature in Hong Kong be 29°C  | stop-loss | $-4.24 | 5.0h
- YES Will the highest temperature in New York City be b | take-profit | $+4.93 | 26.3h
