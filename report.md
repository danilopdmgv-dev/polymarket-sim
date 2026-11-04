# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-11-04 02:32 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1127.75 (-43.6%) | **Cash:** $1014.53 | **Abertas:** 7 | **Ciclos:** 68
**Fechadas:** 127 | **Win rate:** 31% | **PnL realizado:** $-877.38
**Chamadas ao LLM hoje:** 8

## Por motivo de saida
- resolvido: 1 trades, PnL $-46.54
- stop-loss: 87 trades, PnL $-1466.76
- take-profit: 39 trades, PnL $+635.92

## Por categoria
- Clima: 111 trades, win 30%, PnL $-802.06
- Outros: 2 trades, win 50%, PnL $+4.14
- Politica: 14 trades, win 36%, PnL $-79.46
- **Clima INVERSO (compra o lado oposto ao modelo):** 62 trades, win 40%, PnL $-85.55

## Calibracao do LLM vs mercado (454 mercados resolvidos)
- Brier LLM: 0.3010 | Brier mercado: 0.2204 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (338): LLM 0.3419 vs mercado 0.2345
  - Economia/Dados (7): LLM 0.1220 vs mercado 0.1228
  - Entretenimento (26): LLM 0.1406 vs mercado 0.1461
  - Outros (40): LLM 0.1759 vs mercado 0.1737
  - Politica (43): LLM 0.2221 vs mercado 0.2136
- Fonte clima (338): modelo 0.3419 vs mercado 0.2345 -> PERDENDO
- Fonte llm (116): modelo 0.1818 vs mercado 0.1792 -> PERDENDO
- Clima (319): sigma largo 0.3470 | sigma estreito 0.3188 | mercado 0.2358

## Posicoes abertas
- YES Will the highest temperature in Singapore be 32°C on Novembe | entrada 0.41, agora 0.56, LLM 0.16, edge 0.11, medium | Modelo 0.16 vs mercado 0.39
- YES Will the highest temperature in Hong Kong be 28°C on Novembe | entrada 0.56, agora 0.58, LLM 0.25, edge 0.14, medium | Modelo 0.25 vs mercado 0.53
- YES Will the highest temperature in London be 11°C on November 4 | entrada 0.72, agora 0.69, LLM 0.21, edge 0.25, medium | Modelo 0.21 vs mercado 0.68
- YES Will the highest temperature in Paris be 10°C on November 4? | entrada 0.60, agora 0.68, LLM 0.23, edge 0.18, medium | Modelo 0.23 vs mercado 0.57
- YES Will the highest temperature in Karachi be 35°C on November  | entrada 0.43, agora 0.39, LLM 0.26, edge 0.06, medium | Modelo 0.26 vs mercado 0.41
- YES Will the highest temperature in Houston be between 78-79°F o | entrada 0.53, agora 0.53, LLM 0.17, edge 0.17, medium | Modelo 0.17 vs mercado 0.50
- NO Will the Democrats win the Iowa Senate race in 2026? | entrada 0.15, agora 0.15, LLM 0.12, edge 0.35, medium | O mercado esta ligeiramente ineficiente ao precificar os democratas com 87% de chance, superestimand

## Ultimas 10 fechadas
- YES Will the highest temperature in Tel Aviv be 28°C o | take-profit | $+4.01 | 17.6h
- NO Will the Democrats win the Texas Senate race in 20 | stop-loss | $-35.89 | 40.7h
- YES Will the Republicans win the Texas Senate race in  | stop-loss | $-35.95 | 40.8h
- YES Will the highest temperature in Paris be 11°C on N | stop-loss | $-9.19 | 13.2h
- YES Will the highest temperature in Denver be between  | take-profit | $+5.62 | 13.2h
- YES Will the highest temperature in London be 12°C on  | stop-loss | $-5.73 | 13.2h
- YES Will the highest temperature in Tel Aviv be 28°C o | take-profit | $+6.29 | 14.9h
- YES US x Iran ceasefire continues through November 2? | take-profit | $+18.46 | 7.0h
- YES Will the highest temperature in London be 13°C on  | stop-loss | $-8.62 | 7.0h
- YES Will the highest temperature in Dallas be between  | stop-loss | $-12.38 | 13.0h
