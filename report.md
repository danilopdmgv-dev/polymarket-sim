# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-11-06 01:01 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1047.39 (-47.6%) | **Cash:** $1017.50 | **Abertas:** 3 | **Ciclos:** 74
**Fechadas:** 145 | **Win rate:** 30% | **PnL realizado:** $-948.95
**Chamadas ao LLM hoje:** 6

## Por motivo de saida
- resolvido: 3 trades, PnL $-62.42
- stop-loss: 99 trades, PnL $-1559.83
- take-profit: 43 trades, PnL $+673.30

## Por categoria
- Clima: 128 trades, win 30%, PnL $-839.80
- Outros: 2 trades, win 50%, PnL $+4.14
- Politica: 15 trades, win 33%, PnL $-113.30
- **Clima INVERSO (compra o lado oposto ao modelo):** 79 trades, win 38%, PnL $-123.28

## Calibracao do LLM vs mercado (528 mercados resolvidos)
- Brier LLM: 0.2948 | Brier mercado: 0.2159 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (387): LLM 0.3362 vs mercado 0.2338
  - Economia/Dados (7): LLM 0.1220 vs mercado 0.1228
  - Entretenimento (31): LLM 0.1449 vs mercado 0.1494
  - Outros (43): LLM 0.1639 vs mercado 0.1679
  - Politica (60): LLM 0.2193 vs mercado 0.1803
- Fonte clima (387): modelo 0.3362 vs mercado 0.2338 -> PERDENDO
- Fonte llm (141): modelo 0.1812 vs mercado 0.1669 -> PERDENDO
- Clima (368): sigma largo 0.3403 | sigma estreito 0.3141 | mercado 0.2349

## Posicoes abertas
- YES Will the highest temperature in Milan be 11°C on November 6? | entrada 0.46, agora 0.38, LLM 0.21, edge 0.11, medium | Modelo 0.21 vs mercado 0.43
- YES Will the highest temperature in Miami be between 86-87°F on  | entrada 0.63, agora 0.55, LLM 0.12, edge 0.27, medium | Modelo 0.12 vs mercado 0.60
- YES Will the highest temperature in Atlanta be between 74-75°F o | entrada 0.45, agora 0.44, LLM 0.12, edge 0.16, medium | Modelo 0.12 vs mercado 0.43

## Ultimas 10 fechadas
- YES Will the highest temperature in London be 12°C on  | stop-loss | $-4.04 | 4.6h
- YES Will the highest temperature in San Francisco be b | stop-loss | $-3.56 | 4.6h
- YES Will the highest temperature in Cape Town be 20°C  | stop-loss | $-4.09 | 12.1h
- YES Will the highest temperature in Busan be 17°C on N | stop-loss | $-8.24 | 7.6h
- YES Will the highest temperature in Amsterdam be 10°C  | stop-loss | $-4.59 | 7.6h
- YES Will the highest temperature in Miami be between 8 | take-profit | $+14.73 | 26.3h
- YES Will the highest temperature in New York City be b | stop-loss | $-7.25 | 18.7h
- YES Will the highest temperature in Dallas be between  | stop-loss | $-3.73 | 18.7h
- YES Will the highest temperature in London be 11°C on  | stop-loss | $-10.82 | 18.7h
- YES Will the highest temperature in Houston be between | take-profit | $+3.47 | 18.7h
