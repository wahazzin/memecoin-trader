# Paper bot check-in (2026-11-15 00:28 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 722 / 123 / 21 | 722 | 22% | +0.2559 | -0.2188 | **-0.1136** | -81.9994 | 6.269 (top-ups 68.54) | -82.637 | 0 | 0 |
| `m1_random` | 832 / 91 / 112 | 832 | 25% | +0.2571 | -0.2139 | **-0.0973** | -80.9184 | 7.003 (top-ups 68.02) | -81.178 | 0 | 0 |

- Exit reasons: {'take_profit': 389, 'stop_loss': 1016, 'no_volume_15m': 149}
- Sells priced by the verified curve formula because Jupiter had no route: 621
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.214, m1_random +5.856
- Circuit breakers fired: 78
- Stream gaps logged: 88256

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
