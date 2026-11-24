# Paper bot check-in (2026-11-24 00:02 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 984 / 172 / 21 | 984 | 23% | +0.2740 | -0.2149 | **-0.1021** | -100.4826 | 16.922 (top-ups 97.55) | -101.034 | 1 | 0 |
| `m1_random` | 998 / 110 / 115 | 998 | 24% | +0.2533 | -0.2134 | **-0.0993** | -99.0938 | 16.928 (top-ups 96.30) | -99.524 | 0 | 0 |

- Exit reasons: {'take_profit': 489, 'stop_loss': 1291, 'no_volume_15m': 201, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 841
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.911, m1_random +6.627
- Circuit breakers fired: 96
- Stream gaps logged: 103969

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.

## Since amendment B2 (2026-11-24 00:00 UTC, exits from the price paid) — the comparison that counts now

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 3 / 0 / 0 | 2 | 50% | +0.0441 | -0.2550 | **-0.1054** | -0.2109 | 16.922 (top-ups 97.55) | +0.000 | 1 | 0 |
| `m1_random` | 0 / 0 / 0 | 0 | — | +0.0000 | +0.0000 | **—** | +0.0000 | 16.928 (top-ups 96.30) | +0.000 | 0 | 0 |

- Exit reasons: {'stop_loss': 1, 'take_profit': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 1
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.025
- Circuit breakers fired: 0
- Stream gaps logged: 5

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
