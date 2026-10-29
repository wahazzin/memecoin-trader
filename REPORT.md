# Paper bot check-in (2026-10-29 04:12 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 465 / 67 / 12 | 465 | 24% | +0.2670 | -0.2234 | **-0.1074** | -49.9275 | 9.808 (top-ups 39.90) | -50.458 | 0 | 0 |
| `m1_random` | 426 / 46 / 41 | 426 | 23% | +0.2426 | -0.2172 | **-0.1136** | -48.3761 | 11.143 (top-ups 39.64) | -48.959 | 0 | 0 |

- Exit reasons: {'take_profit': 215, 'stop_loss': 597, 'no_volume_15m': 79}
- Sells priced by the verified curve formula because Jupiter had no route: 314
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.785, m1_random +3.388
- Circuit breakers fired: 45
- Stream gaps logged: 53263

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
