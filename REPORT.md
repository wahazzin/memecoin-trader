# Paper bot check-in (2026-11-24 00:23 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 1016 / 182 / 21 | 1011 | 23% | +0.2836 | -0.2147 | **-0.0984** | -99.4551 | 17.496 (top-ups 97.55) | -101.034 | 5 | 0 |
| `m1_random` | 1004 / 110 / 116 | 1002 | 24% | +0.2533 | -0.2134 | **-0.0997** | -99.9242 | 16.357 (top-ups 96.30) | -100.095 | 2 | 0 |

- Exit reasons: {'take_profit': 496, 'stop_loss': 1313, 'no_volume_15m': 203, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 863
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.911, m1_random +6.627
- Circuit breakers fired: 96
- Stream gaps logged: 104035

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.

## Since amendment B2 (2026-11-24 00:00 UTC, exits from the price paid) — the comparison that counts now

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 34 / 10 / 0 | 29 | 34% | +0.4778 | -0.2085 | **+0.0282** | +0.8166 | 17.496 (top-ups 97.55) | -1.239 | 5 | 0 |
| `m1_random` | 6 / 0 / 1 | 4 | 0% | +0.0000 | -0.2076 | **-0.2076** | -0.8304 | 16.357 (top-ups 96.30) | -0.571 | 2 | 0 |

- Exit reasons: {'stop_loss': 23, 'take_profit': 8, 'no_volume_15m': 2}
- Sells priced by the verified curve formula because Jupiter had no route: 23
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.025, m1_random +0.000
- Circuit breakers fired: 0
- Stream gaps logged: 71

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
