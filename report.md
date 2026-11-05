# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-11-05 20:27 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1057.41 (-47.1%) | **Cash:** $995.88 | **Abertas:** 6 | **Ciclos:** 73
**Fechadas:** 142 | **Win rate:** 31% | **PnL realizado:** $-937.26
**Chamadas ao LLM hoje:** 13

## Por motivo de saida
- resolvido: 3 trades, PnL $-62.42
- stop-loss: 96 trades, PnL $-1548.14
- take-profit: 43 trades, PnL $+673.30

## Por categoria
- Clima: 125 trades, win 30%, PnL $-828.11
- Outros: 2 trades, win 50%, PnL $+4.14
- Politica: 15 trades, win 33%, PnL $-113.30
- **Clima INVERSO (compra o lado oposto ao modelo):** 76 trades, win 39%, PnL $-111.59

## Calibracao do LLM vs mercado (517 mercados resolvidos)
- Brier LLM: 0.2934 | Brier mercado: 0.2158 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (376): LLM 0.3355 vs mercado 0.2342
  - Economia/Dados (7): LLM 0.1220 vs mercado 0.1228
  - Entretenimento (31): LLM 0.1449 vs mercado 0.1494
  - Outros (43): LLM 0.1639 vs mercado 0.1679
  - Politica (60): LLM 0.2193 vs mercado 0.1803
- Fonte clima (376): modelo 0.3355 vs mercado 0.2342 -> PERDENDO
- Fonte llm (141): modelo 0.1812 vs mercado 0.1669 -> PERDENDO
- Clima (357): sigma largo 0.3397 | sigma estreito 0.3141 | mercado 0.2353

## Posicoes abertas
- YES Will the highest temperature in Milan be 11°C on November 6? | entrada 0.46, agora 0.39, LLM 0.21, edge 0.11, medium | Modelo 0.21 vs mercado 0.43
- YES Will the highest temperature in Miami be between 86-87°F on  | entrada 0.63, agora 0.56, LLM 0.12, edge 0.27, medium | Modelo 0.12 vs mercado 0.60
- YES Will the highest temperature in Cape Town be 20°C on Novembe | entrada 0.52, agora 0.41, LLM 0.21, edge 0.14, medium | Modelo 0.21 vs mercado 0.49
- YES Will the highest temperature in Atlanta be between 74-75°F o | entrada 0.45, agora 0.45, LLM 0.12, edge 0.16, medium | Modelo 0.12 vs mercado 0.43
- YES Will the highest temperature in San Francisco be between 70- | entrada 0.48, agora 0.48, LLM 0.20, edge 0.13, medium | Modelo 0.20 vs mercado 0.46
- YES Will the highest temperature in London be 12°C on November 6 | entrada 0.37, agora 0.37, LLM 0.19, edge 0.07, medium | Modelo 0.19 vs mercado 0.34

## Ultimas 10 fechadas
- YES Will the highest temperature in Busan be 17°C on N | stop-loss | $-8.24 | 7.6h
- YES Will the highest temperature in Amsterdam be 10°C  | stop-loss | $-4.59 | 7.6h
- YES Will the highest temperature in Miami be between 8 | take-profit | $+14.73 | 26.3h
- YES Will the highest temperature in New York City be b | stop-loss | $-7.25 | 18.7h
- YES Will the highest temperature in Dallas be between  | stop-loss | $-3.73 | 18.7h
- YES Will the highest temperature in London be 11°C on  | stop-loss | $-10.82 | 18.7h
- YES Will the highest temperature in Houston be between | take-profit | $+3.47 | 18.7h
- YES Will the highest temperature in Lucknow be 31°C on | stop-loss | $-10.11 | 4.7h
- YES Will the highest temperature in Houston be between | take-profit | $+9.68 | 21.3h
- NO Will the Democrats win the Iowa Senate race in 202 | resolvido | $-33.83 | 15.6h
