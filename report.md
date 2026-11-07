# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-11-07 14:33 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $989.22 (-50.5%) | **Cash:** $959.99 | **Abertas:** 3 | **Ciclos:** 80 | **KILL SWITCH ATIVO**
**Fechadas:** 159 | **Win rate:** 30% | **PnL realizado:** $-1008.21
**Chamadas ao LLM hoje:** 15

## Por motivo de saida
- resolvido: 3 trades, PnL $-62.42
- stop-loss: 109 trades, PnL $-1654.99
- take-profit: 47 trades, PnL $+709.20

## Por categoria
- Clima: 141 trades, win 30%, PnL $-872.52
- Outros: 2 trades, win 50%, PnL $+4.14
- Politica: 16 trades, win 31%, PnL $-139.83
- **Clima INVERSO (compra o lado oposto ao modelo):** 92 trades, win 37%, PnL $-156.01

## Calibracao do LLM vs mercado (590 mercados resolvidos)
- Brier LLM: 0.2928 | Brier mercado: 0.2175 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (431): LLM 0.3338 vs mercado 0.2351
  - Economia/Dados (9): LLM 0.1526 vs mercado 0.1521
  - Entretenimento (36): LLM 0.1442 vs mercado 0.1478
  - Outros (52): LLM 0.1735 vs mercado 0.1744
  - Politica (62): LLM 0.2142 vs mercado 0.1807
- Fonte clima (431): modelo 0.3338 vs mercado 0.2351 -> PERDENDO
- Fonte llm (159): modelo 0.1816 vs mercado 0.1696 -> PERDENDO
- Clima (412): sigma largo 0.3374 | sigma estreito 0.3126 | mercado 0.2362

## Posicoes abertas
- YES Will the highest temperature in Atlanta be between 66-67°F o | entrada 0.56, agora 0.54, LLM 0.23, edge 0.16, medium | Modelo 0.23 vs mercado 0.54
- YES Will the highest temperature in New York City be between 62- | entrada 0.36, agora 0.30, LLM 0.16, edge 0.09, medium | Modelo 0.16 vs mercado 0.34
- YES Will the highest temperature in Amsterdam be 10°C on Novembe | entrada 0.53, agora 0.51, LLM 0.22, edge 0.15, medium | Modelo 0.22 vs mercado 0.51

## Ultimas 10 fechadas
- YES Will the highest temperature in Chongqing be 17°C  | take-profit | $+3.46 | 6.9h
- YES Will the highest temperature in Madrid be 19°C on  | stop-loss | $-9.50 | 13.1h
- YES Will the highest temperature in Chicago be between | stop-loss | $-9.32 | 13.1h
- YES Will the highest temperature in New York City be b | stop-loss | $-10.61 | 9.9h
- YES Will the highest temperature in Tokyo be 20°C on N | take-profit | $+7.75 | 23.5h
- YES Will the highest temperature in Hong Kong be 28°C  | stop-loss | $-10.83 | 23.5h
- YES Will the highest temperature in Houston be between | stop-loss | $-5.03 | 3.8h
- YES Will the highest temperature in Atlanta be between | stop-loss | $-9.05 | 9.4h
- YES Will the highest temperature in Busan be 14°C on N | stop-loss | $-3.47 | 17.3h
- NO Israel x Iran ceasefire continues through November | stop-loss | $-26.54 | 5.6h
