# Polymarket Survival Sim (v3-alto-volume)
_Atualizado 2026-10-27 05:23 UTC. SIMULACAO, sem dinheiro real._

**Equity:** $1315.70 (-34.2%) | **Cash:** $1057.92 | **Abertas:** 7 | **Ciclos:** 29
**Fechadas:** 41 | **Win rate:** 15% | **PnL realizado:** $-645.14
**Chamadas ao LLM hoje:** 19

## Por motivo de saida
- resolvido: 1 trades, PnL $-46.54
- stop-loss: 34 trades, PnL $-750.40
- take-profit: 6 trades, PnL $+151.80

## Por categoria
- Clima: 36 trades, win 14%, PnL $-542.06
- Outros: 1 trades, win 0%, PnL $-18.51
- Politica: 4 trades, win 25%, PnL $-84.58

## Calibracao do LLM vs mercado (137 mercados resolvidos)
- Brier LLM: 0.3047 | Brier mercado: 0.2170 (menor e melhor)
- **LLM esta PERDENDO do mercado.**
  - Clima (100): LLM 0.3504 vs mercado 0.2273
  - Economia/Dados (4): LLM 0.0341 vs mercado 0.0431
  - Entretenimento (6): LLM 0.2751 vs mercado 0.2832
  - Outros (9): LLM 0.0881 vs mercado 0.0778
  - Politica (18): LLM 0.2293 vs mercado 0.2460
- Fonte clima (100): modelo 0.3504 vs mercado 0.2273 -> PERDENDO
- Fonte llm (37): modelo 0.1813 vs mercado 0.1892 -> GANHANDO
- Clima (81): sigma largo 0.3724 | sigma estreito 0.3349 | mercado 0.2307

## Posicoes abertas
- NO Will the highest temperature in Dallas be between 82-83°F on | entrada 0.63, agora 0.48, LLM 0.19, edge 0.10, medium | Modelo 0.19 vs mercado 0.40
- NO Will Yashar win the most seats in the 2026 Israeli legislati | entrada 0.32, agora 0.26, LLM 0.45, edge 0.11, medium | Market overprices Yashar assuming a clear victory, ignoring severe Knesset fragmentation and strong 
- NO Will the highest temperature in Houston be between 80-81°F o | entrada 0.60, agora 0.59, LLM 0.22, edge 0.09, medium | Modelo 0.22 vs mercado 0.43
- NO Will the highest temperature in Miami be between 82-83°F on  | entrada 0.53, agora 0.39, LLM 0.16, edge 0.18, medium | Modelo 0.16 vs mercado 0.49
- NO Will the highest temperature in Toronto be 9°C on October 27 | entrada 0.60, agora 0.57, LLM 0.23, edge 0.09, medium | Modelo 0.23 vs mercado 0.42
- NO Will the highest temperature in Wellington be 17°C on Octobe | entrada 0.46, agora 0.39, LLM 0.15, edge 0.22, medium | Modelo 0.15 vs mercado 0.57
- NO Will the highest temperature in Munich be 17°C on October 27 | entrada 0.66, agora 0.66, LLM 0.12, edge 0.12, medium | Modelo 0.12 vs mercado 0.38

## Ultimas 10 fechadas
- YES Will Brad Bradford win the 2026 Toronto mayoral el | resolvido | $-46.54 | 8.7h
- NO Will the highest temperature in Singapore be 32°C  | stop-loss | $-40.10 | 14.0h
- NO Will the highest temperature in Jeddah be 37°C on  | stop-loss | $-18.97 | 3.5h
- NO Will the highest temperature in Shanghai be 21°C o | stop-loss | $-17.94 | 8.8h
- NO Will the highest temperature in Munich be 17°C on  | stop-loss | $-16.57 | 8.8h
- NO Will the highest temperature in Dallas be between  | take-profit | $+45.75 | 35.9h
- NO Will the highest temperature in Houston be between | take-profit | $+28.54 | 20.8h
- NO Will the highest temperature in Wellington be 16°C | stop-loss | $-34.70 | 7.0h
- NO Will the highest temperature in New York City be b | stop-loss | $-42.23 | 7.0h
- NO Will the highest temperature in Toronto be 16°C on | stop-loss | $-35.80 | 12.8h
