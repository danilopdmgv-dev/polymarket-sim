# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-11-04 18:11 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1080.25 (-46.0%) | **Cash:** $1011.04 | **Abertas:** 6 | **Ciclos:** 69
**Fechadas:** 133 | **Win rate:** 31% | **PnL realizado:** $-920.41
**Chamadas ao LLM hoje:** 16

## Por motivo de saida
- resolvido: 3 trades, PnL $-62.42
- stop-loss: 90 trades, PnL $-1503.40
- take-profit: 40 trades, PnL $+645.42

## Por categoria
- Clima: 116 trades, win 30%, PnL $-811.26
- Outros: 2 trades, win 50%, PnL $+4.14
- Politica: 15 trades, win 33%, PnL $-113.30
- **Clima INVERSO (compra o lado oposto ao modelo):** 67 trades, win 40%, PnL $-94.74

## Calibracao do LLM vs mercado (469 mercados resolvidos)
- Brier LLM: 0.3035 | Brier mercado: 0.2200 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (352): LLM 0.3422 vs mercado 0.2340
  - Economia/Dados (7): LLM 0.1220 vs mercado 0.1228
  - Entretenimento (26): LLM 0.1406 vs mercado 0.1461
  - Outros (40): LLM 0.1759 vs mercado 0.1737
  - Politica (44): LLM 0.2346 vs mercado 0.2091
- Fonte clima (352): modelo 0.3422 vs mercado 0.2340 -> PERDENDO
- Fonte llm (117): modelo 0.1869 vs mercado 0.1778 -> PERDENDO
- Clima (333): sigma largo 0.3471 | sigma estreito 0.3197 | mercado 0.2353

## Posicoes abertas
- YES Will the highest temperature in Houston be between 78-79°F o | entrada 0.53, agora 0.56, LLM 0.17, edge 0.17, medium | Modelo 0.17 vs mercado 0.50
- YES Will the highest temperature in Houston be between 82-83°F o | entrada 0.47, agora 0.47, LLM 0.10, edge 0.19, medium | Modelo 0.10 vs mercado 0.45
- YES Will the highest temperature in London be 11°C on November 5 | entrada 0.62, agora 0.62, LLM 0.22, edge 0.21, medium | Modelo 0.22 vs mercado 0.60
- YES Will the highest temperature in Dallas be between 78-79°F on | entrada 0.59, agora 0.59, LLM 0.18, edge 0.21, medium | Modelo 0.18 vs mercado 0.57
- YES Will the highest temperature in New York City be between 70- | entrada 0.52, agora 0.52, LLM 0.21, edge 0.15, medium | Modelo 0.21 vs mercado 0.50
- YES Will the highest temperature in Miami be between 84-85°F on  | entrada 0.41, agora 0.41, LLM 0.19, edge 0.09, medium | Modelo 0.19 vs mercado 0.38

## Ultimas 10 fechadas
- NO Will the Democrats win the Iowa Senate race in 202 | resolvido | $-33.83 | 15.6h
- YES Will the highest temperature in Karachi be 35°C on | stop-loss | $-12.15 | 20.0h
- YES Will the highest temperature in Paris be 10°C on N | stop-loss | $-12.23 | 20.0h
- YES Will the highest temperature in London be 11°C on  | stop-loss | $-12.26 | 20.0h
- YES Will the highest temperature in Hong Kong be 28°C  | take-profit | $+9.50 | 25.3h
- YES Will the highest temperature in Singapore be 32°C  | resolvido | $+17.95 | 33.2h
- YES Will the highest temperature in Tel Aviv be 28°C o | take-profit | $+4.01 | 17.6h
- NO Will the Democrats win the Texas Senate race in 20 | stop-loss | $-35.89 | 40.7h
- YES Will the Republicans win the Texas Senate race in  | stop-loss | $-35.95 | 40.8h
- YES Will the highest temperature in Paris be 11°C on N | stop-loss | $-9.19 | 13.2h
