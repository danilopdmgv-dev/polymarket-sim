# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-11-05 12:53 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1057.46 (-47.1%) | **Cash:** $993.74 | **Abertas:** 6 | **Ciclos:** 72
**Fechadas:** 139 | **Win rate:** 31% | **PnL realizado:** $-939.16
**Chamadas ao LLM hoje:** 5

## Por motivo de saida
- resolvido: 3 trades, PnL $-62.42
- stop-loss: 94 trades, PnL $-1535.31
- take-profit: 42 trades, PnL $+658.57

## Por categoria
- Clima: 122 trades, win 30%, PnL $-830.01
- Outros: 2 trades, win 50%, PnL $+4.14
- Politica: 15 trades, win 33%, PnL $-113.30
- **Clima INVERSO (compra o lado oposto ao modelo):** 73 trades, win 40%, PnL $-113.49

## Calibracao do LLM vs mercado (506 mercados resolvidos)
- Brier LLM: 0.2980 | Brier mercado: 0.2161 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (365): LLM 0.3431 vs mercado 0.2351
  - Economia/Dados (7): LLM 0.1220 vs mercado 0.1228
  - Entretenimento (31): LLM 0.1449 vs mercado 0.1494
  - Outros (43): LLM 0.1639 vs mercado 0.1679
  - Politica (60): LLM 0.2193 vs mercado 0.1803
- Fonte clima (365): modelo 0.3431 vs mercado 0.2351 -> PERDENDO
- Fonte llm (141): modelo 0.1812 vs mercado 0.1669 -> PERDENDO
- Clima (346): sigma largo 0.3478 | sigma estreito 0.3205 | mercado 0.2364

## Posicoes abertas
- YES Will the highest temperature in Miami be between 84-85°F on  | entrada 0.41, agora 0.36, LLM 0.19, edge 0.09, medium | Modelo 0.19 vs mercado 0.38
- YES Will the highest temperature in Milan be 11°C on November 6? | entrada 0.46, agora 0.38, LLM 0.21, edge 0.11, medium | Modelo 0.21 vs mercado 0.43
- YES Will the highest temperature in Miami be between 86-87°F on  | entrada 0.63, agora 0.63, LLM 0.12, edge 0.27, medium | Modelo 0.12 vs mercado 0.60
- YES Will the highest temperature in Amsterdam be 10°C on Novembe | entrada 0.42, agora 0.42, LLM 0.18, edge 0.09, medium | Modelo 0.18 vs mercado 0.39
- YES Will the highest temperature in Busan be 17°C on November 6? | entrada 0.44, agora 0.44, LLM 0.10, edge 0.17, medium | Modelo 0.10 vs mercado 0.41
- YES Will the highest temperature in Cape Town be 20°C on Novembe | entrada 0.52, agora 0.52, LLM 0.21, edge 0.14, medium | Modelo 0.21 vs mercado 0.49

## Ultimas 10 fechadas
- YES Will the highest temperature in New York City be b | stop-loss | $-7.25 | 18.7h
- YES Will the highest temperature in Dallas be between  | stop-loss | $-3.73 | 18.7h
- YES Will the highest temperature in London be 11°C on  | stop-loss | $-10.82 | 18.7h
- YES Will the highest temperature in Houston be between | take-profit | $+3.47 | 18.7h
- YES Will the highest temperature in Lucknow be 31°C on | stop-loss | $-10.11 | 4.7h
- YES Will the highest temperature in Houston be between | take-profit | $+9.68 | 21.3h
- NO Will the Democrats win the Iowa Senate race in 202 | resolvido | $-33.83 | 15.6h
- YES Will the highest temperature in Karachi be 35°C on | stop-loss | $-12.15 | 20.0h
- YES Will the highest temperature in Paris be 10°C on N | stop-loss | $-12.23 | 20.0h
- YES Will the highest temperature in London be 11°C on  | stop-loss | $-12.26 | 20.0h
