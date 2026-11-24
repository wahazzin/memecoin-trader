# Paper bot check-in (2026-11-24 00:38 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 1035 / 183 / 21 | 1034 | 23% | +0.2806 | -0.2143 | **-0.0989** | -102.2876 | 15.023 (top-ups 97.55) | -102.889 | 1 | 0 |
| `m1_random` | 1009 / 111 / 116 | 1006 | 24% | +0.2527 | -0.2131 | **-0.0992** | -99.8043 | 16.072 (top-ups 96.30) | -100.466 | 3 | 0 |

- Exit reasons: {'take_profit': 498, 'stop_loss': 1332, 'no_volume_15m': 209, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 879
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.975, m1_random +6.637
- Circuit breakers fired: 96
- Stream gaps logged: 104101

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.

## Since amendment B2 (2026-11-24 00:00 UTC, exits from the price paid) — the comparison that counts now

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 53 / 11 / 0 | 52 | 29% | +0.3643 | -0.2022 | **-0.0388** | -2.0160 | 15.023 (top-ups 97.55) | -3.712 | 1 | 0 |
| `m1_random` | 11 / 1 / 1 | 8 | 25% | +0.1830 | -0.1794 | **-0.0888** | -0.7106 | 16.072 (top-ups 96.30) | -0.942 | 3 | 0 |

- Exit reasons: {'stop_loss': 42, 'take_profit': 10, 'no_volume_15m': 8}
- Sells priced by the verified curve formula because Jupiter had no route: 39
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.089, m1_random +0.010
- Circuit breakers fired: 0
- Stream gaps logged: 138

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
