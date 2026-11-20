# Paper bot check-in (2026-11-20 00:11 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 865 / 153 / 21 | 865 | 22% | +0.2742 | -0.2167 | **-0.1066** | -92.2183 | 10.669 (top-ups 83.24) | -93.619 | 0 | 0 |
| `m1_random` | 937 / 106 / 114 | 937 | 25% | +0.2538 | -0.2139 | **-0.0986** | -92.4199 | 10.062 (top-ups 82.11) | -92.207 | 0 | 0 |

- Exit reasons: {'take_profit': 445, 'stop_loss': 1180, 'no_volume_15m': 176, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 755
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.604, m1_random +6.455
- Circuit breakers fired: 88
- Stream gaps logged: 97104

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
