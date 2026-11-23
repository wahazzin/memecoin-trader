# W1 results 

positions: 5991287 (design 4772013, holdout 1219274); eligible wallets: 27442; top group: 50; with ≥5 holdout closed positions: top 43, others 7388

## W1a — do the design-period top wallets keep winning in the holdout?

| Group | Wallets | Mean holdout P&L / closed position (SOL) | 95% CI |
|---|---|---|---|
| Top 50 | 43 | +0.4436 | +0.2781 … +0.6332 |
| Other eligible | 7388 | -0.0406 | — |

Top minus others: 95% CI +0.3199 … +0.6670. Spearman design vs holdout (all eligible, reported only): +0.435

**W1a: PASS**

## W1b — copying them (buy/sell after the wallet, real reserves, all costs, 0.5 SOL)

| Copy | Delay | n | Win rate | Expectancy/trade | t (hours) | vs random-wallet copy: diff | t |
|---|---|---|---|---|---|---|---|
| top 50 **(primary)** | 2 s | 23406 | 21% | -14.89% | -34.05 | +6.76% | +13.64 |
| top 50 | 1 s | 23419 | 22% | -12.51% | -26.64 | +7.16% | +13.02 |
| top 50 | 5 s | 23386 | 17% | -19.59% | -43.22 | +5.83% | +9.85 |
| top 10 | 2 s | 8517 | 21% | -14.96% | -28.57 | +7.90% | +8.39 |
| top 10 | 1 s | 8521 | 23% | -11.07% | -23.75 | +10.24% | +13.09 |
| top 10 | 5 s | 8507 | 17% | -20.75% | -34.33 | +5.24% | +6.02 |

**W1b (primary: top 50, 2 s delay): NO EVIDENCE**

Pre-registered: W1a = top group's holdout mean > 0 AND beats other eligible wallets (95% bootstrap CIs above 0). W1b = copy expectancy > 0 with t ≥ 2 AND beats random-wallet copy with t ≥ 2, ≥ 300 copied trades. Rows other than the primary are reported only. See research/W1_PREREG.md.

Data quality (amendment B-data, counted over all passes): {'curve_outages': 1716, 'swap_outages': 838, 'curve_outage_s': 279679, 'coins': 333096, 'excluded_swap_outage': 21122, 'excluded_curve_outage': 378443}

