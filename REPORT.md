# Paper bot check-in (2026-11-20 00:21 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 867 / 154 / 21 | 867 | 22% | +0.2742 | -0.2170 | **-0.1071** | -92.8500 | 10.034 (top-ups 83.24) | -93.619 | 0 | 0 |
| `m1_random` | 937 / 106 / 114 | 937 | 25% | +0.2538 | -0.2139 | **-0.0986** | -92.4199 | 9.428 (top-ups 82.11) | -92.841 | 0 | 0 |

- Exit reasons: {'take_profit': 445, 'stop_loss': 1182, 'no_volume_15m': 176, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 756
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.612, m1_random +6.455
- Circuit breakers fired: 88
- Stream gaps logged: 97116

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
