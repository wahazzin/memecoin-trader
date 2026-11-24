# Paper bot check-in (2026-11-24 00:33 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 1032 / 183 / 21 | 1029 | 23% | +0.2812 | -0.2145 | **-0.0989** | -101.7512 | 16.510 (top-ups 97.55) | -101.402 | 3 | 0 |
| `m1_random` | 1008 / 110 / 116 | 1006 | 24% | +0.2527 | -0.2131 | **-0.0992** | -99.8043 | 16.117 (top-ups 96.30) | -100.466 | 2 | 0 |

- Exit reasons: {'take_profit': 497, 'stop_loss': 1330, 'no_volume_15m': 207, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 876
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.975, m1_random +6.637
- Circuit breakers fired: 96
- Stream gaps logged: 104071

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.

## Since amendment B2 (2026-11-24 00:00 UTC, exits from the price paid) — the comparison that counts now

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 50 / 11 / 0 | 47 | 30% | +0.3809 | -0.2064 | **-0.0315** | -1.4795 | 16.510 (top-ups 97.55) | -2.224 | 3 | 0 |
| `m1_random` | 10 / 0 / 1 | 8 | 25% | +0.1830 | -0.1794 | **-0.0888** | -0.7106 | 16.117 (top-ups 96.30) | -0.942 | 2 | 0 |

- Exit reasons: {'stop_loss': 40, 'take_profit': 9, 'no_volume_15m': 6}
- Sells priced by the verified curve formula because Jupiter had no route: 36
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.089, m1_random +0.010
- Circuit breakers fired: 0
- Stream gaps logged: 107

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
