# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-11-08 08:40 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $984.09 (-50.8%) | **Cash:** $970.96 | **Abertas:** 1 | **Ciclos:** 84 | **KILL SWITCH ATIVO**
**Fechadas:** 161 | **Win rate:** 30% | **PnL realizado:** $-1018.49
**Chamadas ao LLM hoje:** 0

## Por motivo de saida
- resolvido: 3 trades, PnL $-62.42
- stop-loss: 111 trades, PnL $-1665.27
- take-profit: 47 trades, PnL $+709.20

## Por categoria
- Clima: 143 trades, win 29%, PnL $-882.80
- Outros: 2 trades, win 50%, PnL $+4.14
- Politica: 16 trades, win 31%, PnL $-139.83
- **Clima INVERSO (compra o lado oposto ao modelo):** 94 trades, win 36%, PnL $-166.29

## Calibracao do LLM vs mercado (613 mercados resolvidos)
- Brier LLM: 0.2938 | Brier mercado: 0.2169 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (453): LLM 0.3336 vs mercado 0.2338
  - Economia/Dados (9): LLM 0.1526 vs mercado 0.1521
  - Entretenimento (36): LLM 0.1442 vs mercado 0.1478
  - Outros (53): LLM 0.1725 vs mercado 0.1731
  - Politica (62): LLM 0.2142 vs mercado 0.1807
- Fonte clima (453): modelo 0.3336 vs mercado 0.2338 -> PERDENDO
- Fonte llm (160): modelo 0.1812 vs mercado 0.1691 -> PERDENDO
- Clima (434): sigma largo 0.3369 | sigma estreito 0.3130 | mercado 0.2347

## Posicoes abertas
- YES Will the highest temperature in Amsterdam be 10°C on Novembe | entrada 0.53, agora 0.66, LLM 0.22, edge 0.15, medium | Modelo 0.22 vs mercado 0.51

## Ultimas 10 fechadas
- YES Will the highest temperature in New York City be b | stop-loss | $-5.43 | 15.2h
- YES Will the highest temperature in Atlanta be between | stop-loss | $-4.85 | 17.7h
- YES Will the highest temperature in Chongqing be 17°C  | take-profit | $+3.46 | 6.9h
- YES Will the highest temperature in Madrid be 19°C on  | stop-loss | $-9.50 | 13.1h
- YES Will the highest temperature in Chicago be between | stop-loss | $-9.32 | 13.1h
- YES Will the highest temperature in New York City be b | stop-loss | $-10.61 | 9.9h
- YES Will the highest temperature in Tokyo be 20°C on N | take-profit | $+7.75 | 23.5h
- YES Will the highest temperature in Hong Kong be 28°C  | stop-loss | $-10.83 | 23.5h
- YES Will the highest temperature in Houston be between | stop-loss | $-5.03 | 3.8h
- YES Will the highest temperature in Atlanta be between | stop-loss | $-9.05 | 9.4h
