# Paper bot check-in (2026-11-24 00:49 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 1044 / 183 / 21 | 1043 | 23% | +0.2817 | -0.2141 | **-0.0986** | -102.8155 | 14.286 (top-ups 97.55) | -103.626 | 1 | 0 |
| `m1_random` | 1011 / 111 / 116 | 1010 | 24% | +0.2529 | -0.2129 | **-0.0990** | -99.9625 | 16.030 (top-ups 96.30) | -100.576 | 1 | 0 |

- Exit reasons: {'take_profit': 501, 'stop_loss': 1339, 'no_volume_15m': 212, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 887
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +3.045, m1_random +6.637
- Circuit breakers fired: 97
- Stream gaps logged: 104156

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.

## Since amendment B2 (2026-11-24 00:00 UTC, exits from the price paid) — the comparison that counts now

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 62 / 11 / 0 | 61 | 28% | +0.3706 | -0.2010 | **-0.0417** | -2.5438 | 14.286 (top-ups 97.55) | -4.449 | 1 | 0 |
| `m1_random` | 13 / 1 / 1 | 12 | 25% | +0.2272 | -0.1723 | **-0.0724** | -0.8687 | 16.030 (top-ups 96.30) | -1.052 | 1 | 0 |

- Exit reasons: {'stop_loss': 49, 'take_profit': 13, 'no_volume_15m': 11}
- Sells priced by the verified curve formula because Jupiter had no route: 47
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.159, m1_random +0.010
- Circuit breakers fired: 1
- Stream gaps logged: 192

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
