# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-11-06 16:06 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1057.00 (-47.2%) | **Cash:** $949.53 | **Abertas:** 7 | **Ciclos:** 76
**Fechadas:** 147 | **Win rate:** 31% | **PnL realizado:** $-941.69
**Chamadas ao LLM hoje:** 22

## Por motivo de saida
- resolvido: 3 trades, PnL $-62.42
- stop-loss: 100 trades, PnL $-1564.82
- take-profit: 44 trades, PnL $+685.54

## Por categoria
- Clima: 130 trades, win 30%, PnL $-832.54
- Outros: 2 trades, win 50%, PnL $+4.14
- Politica: 15 trades, win 33%, PnL $-113.30
- **Clima INVERSO (compra o lado oposto ao modelo):** 81 trades, win 38%, PnL $-116.02

## Calibracao do LLM vs mercado (550 mercados resolvidos)
- Brier LLM: 0.2957 | Brier mercado: 0.2177 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (406): LLM 0.3362 vs mercado 0.2355
  - Economia/Dados (7): LLM 0.1220 vs mercado 0.1228
  - Entretenimento (31): LLM 0.1449 vs mercado 0.1494
  - Outros (46): LLM 0.1658 vs mercado 0.1693
  - Politica (60): LLM 0.2193 vs mercado 0.1803
- Fonte clima (406): modelo 0.3362 vs mercado 0.2355 -> PERDENDO
- Fonte llm (144): modelo 0.1815 vs mercado 0.1673 -> PERDENDO
- Clima (387): sigma largo 0.3401 | sigma estreito 0.3149 | mercado 0.2366

## Posicoes abertas
- YES Will the highest temperature in Atlanta be between 74-75°F o | entrada 0.45, agora 0.45, LLM 0.12, edge 0.16, medium | Modelo 0.12 vs mercado 0.43
- YES Will the highest temperature in Hong Kong be 28°C on Novembe | entrada 0.47, agora 0.49, LLM 0.20, edge 0.13, medium | Modelo 0.20 vs mercado 0.45
- YES Will the highest temperature in Tokyo be 20°C on November 7? | entrada 0.56, agora 0.50, LLM 0.18, edge 0.18, medium | Modelo 0.18 vs mercado 0.53
- YES Will the highest temperature in Busan be 14°C on November 7? | entrada 0.59, agora 0.56, LLM 0.14, edge 0.22, medium | Modelo 0.14 vs mercado 0.56
- YES Will the highest temperature in Chicago be between 48-49°F o | entrada 0.48, agora 0.48, LLM 0.22, edge 0.13, medium | Modelo 0.22 vs mercado 0.46
- YES Will the highest temperature in Atlanta be between 64-65°F o | entrada 0.47, agora 0.47, LLM 0.25, edge 0.09, medium | Modelo 0.25 vs mercado 0.45
- NO Israel x Iran ceasefire continues through November 7? | entrada 0.11, agora 0.11, LLM 0.15, edge 0.36, high | O mercado subestima a gravidade dos ataques recem-reportados de Israel e EUA em 6 de novembro.

## Ultimas 10 fechadas
- YES Will the highest temperature in Miami be between 8 | stop-loss | $-4.98 | 27.2h
- YES Will the highest temperature in Milan be 11°C on N | take-profit | $+12.24 | 35.6h
- YES Will the highest temperature in London be 12°C on  | stop-loss | $-4.04 | 4.6h
- YES Will the highest temperature in San Francisco be b | stop-loss | $-3.56 | 4.6h
- YES Will the highest temperature in Cape Town be 20°C  | stop-loss | $-4.09 | 12.1h
- YES Will the highest temperature in Busan be 17°C on N | stop-loss | $-8.24 | 7.6h
- YES Will the highest temperature in Amsterdam be 10°C  | stop-loss | $-4.59 | 7.6h
- YES Will the highest temperature in Miami be between 8 | take-profit | $+14.73 | 26.3h
- YES Will the highest temperature in New York City be b | stop-loss | $-7.25 | 18.7h
- YES Will the highest temperature in Dallas be between  | stop-loss | $-3.73 | 18.7h
