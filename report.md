# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-10-27 00:11 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1425.01 (-28.7%) | **Cash:** $1094.59 | **Abertas:** 8 | **Ciclos:** 28
**Fechadas:** 39 | **Win rate:** 15% | **PnL realizado:** $-558.50
**Chamadas ao LLM hoje:** 10

## Por motivo de saida
- stop-loss: 33 trades, PnL $-710.30
- take-profit: 6 trades, PnL $+151.80

## Por categoria
- Clima: 35 trades, win 14%, PnL $-501.95
- Outros: 1 trades, win 0%, PnL $-18.51
- Politica: 3 trades, win 33%, PnL $-38.04

## Calibracao do LLM vs mercado (124 mercados resolvidos)
- Brier LLM: 0.3033 | Brier mercado: 0.2192 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (91): LLM 0.3445 vs mercado 0.2268
  - Economia/Dados (4): LLM 0.0341 vs mercado 0.0431
  - Entretenimento (5): LLM 0.3056 vs mercado 0.3154
  - Outros (8): LLM 0.0760 vs mercado 0.0650
  - Politica (16): LLM 0.2495 vs mercado 0.2672
- Fonte clima (91): modelo 0.3445 vs mercado 0.2268 -> PERDENDO
- Fonte llm (33): modelo 0.1898 vs mercado 0.1983 -> GANHANDO
- Clima (72): sigma largo 0.3676 | sigma estreito 0.3366 | mercado 0.2305

## Posicoes abertas
- NO Will the highest temperature in Dallas be between 82-83°F on | entrada 0.63, agora 0.51, LLM 0.19, edge 0.10, medium | Modelo 0.19 vs mercado 0.40
- NO Will the highest temperature in Singapore be 32°C on October | entrada 0.50, agora 0.47, LLM 0.20, edge 0.17, medium | Modelo 0.20 vs mercado 0.52
- NO Will Yashar win the most seats in the 2026 Israeli legislati | entrada 0.32, agora 0.31, LLM 0.45, edge 0.11, medium | Market overprices Yashar assuming a clear victory, ignoring severe Knesset fragmentation and strong 
- YES Will Brad Bradford win the 2026 Toronto mayoral election? | entrada 0.22, agora 0.20, LLM 0.44, edge 0.10, high | O mercado subestima a força de Bradford na reta final ao precificar suas chances em apenas 20%, enqu
- NO Will the highest temperature in Houston be between 80-81°F o | entrada 0.60, agora 0.60, LLM 0.22, edge 0.09, medium | Modelo 0.22 vs mercado 0.43
- NO Will the highest temperature in Miami be between 82-83°F on  | entrada 0.53, agora 0.53, LLM 0.16, edge 0.18, medium | Modelo 0.16 vs mercado 0.49
- NO Will the highest temperature in Toronto be 9°C on October 27 | entrada 0.60, agora 0.60, LLM 0.23, edge 0.09, medium | Modelo 0.23 vs mercado 0.42
- NO Will the highest temperature in Wellington be 17°C on Octobe | entrada 0.46, agora 0.46, LLM 0.15, edge 0.22, medium | Modelo 0.15 vs mercado 0.57

## Ultimas 10 fechadas
- NO Will the highest temperature in Jeddah be 37°C on  | stop-loss | $-18.97 | 3.5h
- NO Will the highest temperature in Shanghai be 21°C o | stop-loss | $-17.94 | 8.8h
- NO Will the highest temperature in Munich be 17°C on  | stop-loss | $-16.57 | 8.8h
- NO Will the highest temperature in Dallas be between  | take-profit | $+45.75 | 35.9h
- NO Will the highest temperature in Houston be between | take-profit | $+28.54 | 20.8h
- NO Will the highest temperature in Wellington be 16°C | stop-loss | $-34.70 | 7.0h
- NO Will the highest temperature in New York City be b | stop-loss | $-42.23 | 7.0h
- NO Will the highest temperature in Toronto be 16°C on | stop-loss | $-35.80 | 12.8h
- NO Will the highest temperature in Amsterdam be 13°C  | stop-loss | $-15.06 | 5.8h
- NO Will the highest temperature in Milan be 16°C on O | stop-loss | $-15.86 | 8.5h
