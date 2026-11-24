# Paper bot check-in (2026-11-24 00:44 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 1041 / 183 / 21 | 1040 | 23% | +0.2817 | -0.2143 | **-0.0984** | -102.3315 | 15.213 (top-ups 97.55) | -102.889 | 1 | 0 |
| `m1_random` | 1011 / 111 / 116 | 1007 | 24% | +0.2527 | -0.2133 | **-0.0995** | -100.1534 | 15.876 (top-ups 96.30) | -100.576 | 4 | 0 |

- Exit reasons: {'take_profit': 500, 'stop_loss': 1336, 'no_volume_15m': 210, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 884
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.975, m1_random +6.637
- Circuit breakers fired: 96
- Stream gaps logged: 104132

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.

## Since amendment B2 (2026-11-24 00:00 UTC, exits from the price paid) — the comparison that counts now

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 59 / 11 / 0 | 58 | 29% | +0.3706 | -0.2039 | **-0.0355** | -2.0599 | 15.213 (top-ups 97.55) | -3.712 | 1 | 0 |
| `m1_random` | 13 / 1 / 1 | 9 | 22% | +0.1830 | -0.2037 | **-0.1177** | -1.0596 | 15.876 (top-ups 96.30) | -1.052 | 4 | 0 |

- Exit reasons: {'stop_loss': 46, 'take_profit': 12, 'no_volume_15m': 9}
- Sells priced by the verified curve formula because Jupiter had no route: 44
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.089, m1_random +0.010
- Circuit breakers fired: 0
- Stream gaps logged: 168

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
