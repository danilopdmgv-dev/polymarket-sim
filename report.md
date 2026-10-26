# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-10-26 15:26 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1430.29 (-28.5%) | **Cash:** $1150.23 | **Abertas:** 6 | **Ciclos:** 26
**Fechadas:** 34 | **Win rate:** 12% | **PnL realizado:** $-579.31
**Chamadas ao LLM hoje:** 24

## Por motivo de saida
- stop-loss: 30 trades, PnL $-656.82
- take-profit: 4 trades, PnL $+77.51

## Por categoria
- Clima: 30 trades, win 10%, PnL $-522.76
- Outros: 1 trades, win 0%, PnL $-18.51
- Politica: 3 trades, win 33%, PnL $-38.04

## Calibracao do LLM vs mercado (107 mercados resolvidos)
- Brier LLM: 0.2937 | Brier mercado: 0.2197 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (74): LLM 0.3400 vs mercado 0.2293
  - Economia/Dados (4): LLM 0.0341 vs mercado 0.0431
  - Entretenimento (5): LLM 0.3056 vs mercado 0.3154
  - Outros (8): LLM 0.0760 vs mercado 0.0650
  - Politica (16): LLM 0.2495 vs mercado 0.2672
- Fonte clima (74): modelo 0.3400 vs mercado 0.2293 -> PERDENDO
- Fonte llm (33): modelo 0.1898 vs mercado 0.1983 -> GANHANDO
- Clima (55): sigma largo 0.3687 | sigma estreito 0.3389 | mercado 0.2351

## Posicoes abertas
- NO Will the highest temperature in Dallas be between 80-81°F on | entrada 0.49, agora 0.54, LLM 0.25, edge 0.15, medium | Modelo 0.25 vs mercado 0.54
- NO Will the highest temperature in Houston be between 80-81°F o | entrada 0.60, agora 0.65, LLM 0.20, edge 0.10, medium | Modelo 0.20 vs mercado 0.45
- NO Will the highest temperature in Dallas be between 82-83°F on | entrada 0.63, agora 0.63, LLM 0.19, edge 0.10, medium | Modelo 0.19 vs mercado 0.40
- NO Will the highest temperature in Singapore be 32°C on October | entrada 0.50, agora 0.50, LLM 0.20, edge 0.17, medium | Modelo 0.20 vs mercado 0.52
- NO Will the highest temperature in Munich be 17°C on October 27 | entrada 0.56, agora 0.56, LLM 0.15, edge 0.16, medium | Modelo 0.15 vs mercado 0.47
- NO Will the highest temperature in Shanghai be 21°C on October  | entrada 0.40, agora 0.40, LLM 0.22, edge 0.22, medium | Modelo 0.22 vs mercado 0.64

## Ultimas 10 fechadas
- NO Will the highest temperature in Wellington be 16°C | stop-loss | $-34.70 | 7.0h
- NO Will the highest temperature in New York City be b | stop-loss | $-42.23 | 7.0h
- NO Will the highest temperature in Toronto be 16°C on | stop-loss | $-35.80 | 12.8h
- NO Will the highest temperature in Amsterdam be 13°C  | stop-loss | $-15.06 | 5.8h
- NO Will the highest temperature in Milan be 16°C on O | stop-loss | $-15.86 | 8.5h
- NO Will the highest temperature in Beijing be 19°C on | stop-loss | $-47.47 | 15.7h
- NO Will the highest temperature in Chengdu be 20°C on | stop-loss | $-26.22 | 4.6h
- NO Will the highest temperature in Paris be 15°C on O | stop-loss | $-15.29 | 9.9h
- NO Will the highest temperature in Wellington be 17°C | take-profit | $+32.10 | 7.2h
- NO Will the highest temperature in Amsterdam be 14°C  | take-profit | $+13.51 | 7.2h
