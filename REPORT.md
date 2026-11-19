# Paper bot check-in (2026-11-19 02:30 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 864 / 152 / 21 | 864 | 22% | +0.2720 | -0.2167 | **-0.1075** | -92.9042 | 9.982 (top-ups 83.24) | -93.619 | 0 | 0 |
| `m1_random` | 934 / 106 / 114 | 934 | 25% | +0.2538 | -0.2134 | **-0.0979** | -91.4205 | 10.428 (top-ups 82.11) | -91.842 | 0 | 0 |

- Exit reasons: {'take_profit': 445, 'stop_loss': 1176, 'no_volume_15m': 176, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 754
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.604, m1_random +6.420
- Circuit breakers fired: 87
- Stream gaps logged: 95142

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
