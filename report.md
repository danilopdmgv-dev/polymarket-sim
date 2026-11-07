# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-11-07 19:13 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $985.55 (-50.7%) | **Cash:** $965.85 | **Abertas:** 2 | **Ciclos:** 81 | **KILL SWITCH ATIVO**
**Fechadas:** 160 | **Win rate:** 30% | **PnL realizado:** $-1013.06
**Chamadas ao LLM hoje:** 15

## Por motivo de saida
- resolvido: 3 trades, PnL $-62.42
- stop-loss: 110 trades, PnL $-1659.84
- take-profit: 47 trades, PnL $+709.20

## Por categoria
- Clima: 142 trades, win 30%, PnL $-877.37
- Outros: 2 trades, win 50%, PnL $+4.14
- Politica: 16 trades, win 31%, PnL $-139.83
- **Clima INVERSO (compra o lado oposto ao modelo):** 93 trades, win 37%, PnL $-160.85

## Calibracao do LLM vs mercado (596 mercados resolvidos)
- Brier LLM: 0.2957 | Brier mercado: 0.2171 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (437): LLM 0.3372 vs mercado 0.2344
  - Economia/Dados (9): LLM 0.1526 vs mercado 0.1521
  - Entretenimento (36): LLM 0.1442 vs mercado 0.1478
  - Outros (52): LLM 0.1735 vs mercado 0.1744
  - Politica (62): LLM 0.2142 vs mercado 0.1807
- Fonte clima (437): modelo 0.3372 vs mercado 0.2344 -> PERDENDO
- Fonte llm (159): modelo 0.1816 vs mercado 0.1696 -> PERDENDO
- Clima (418): sigma largo 0.3409 | sigma estreito 0.3161 | mercado 0.2354

## Posicoes abertas
- YES Will the highest temperature in New York City be between 62- | entrada 0.36, agora 0.32, LLM 0.16, edge 0.09, medium | Modelo 0.16 vs mercado 0.34
- YES Will the highest temperature in Amsterdam be 10°C on Novembe | entrada 0.53, agora 0.52, LLM 0.22, edge 0.15, medium | Modelo 0.22 vs mercado 0.51

## Ultimas 10 fechadas
- YES Will the highest temperature in Atlanta be between | stop-loss | $-4.85 | 17.7h
- YES Will the highest temperature in Chongqing be 17°C  | take-profit | $+3.46 | 6.9h
- YES Will the highest temperature in Madrid be 19°C on  | stop-loss | $-9.50 | 13.1h
- YES Will the highest temperature in Chicago be between | stop-loss | $-9.32 | 13.1h
- YES Will the highest temperature in New York City be b | stop-loss | $-10.61 | 9.9h
- YES Will the highest temperature in Tokyo be 20°C on N | take-profit | $+7.75 | 23.5h
- YES Will the highest temperature in Hong Kong be 28°C  | stop-loss | $-10.83 | 23.5h
- YES Will the highest temperature in Houston be between | stop-loss | $-5.03 | 3.8h
- YES Will the highest temperature in Atlanta be between | stop-loss | $-9.05 | 9.4h
- YES Will the highest temperature in Busan be 14°C on N | stop-loss | $-3.47 | 17.3h
