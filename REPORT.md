# Paper bot check-in (2026-11-17 00:59 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 793 / 136 / 21 | 791 | 23% | +0.2597 | -0.2196 | **-0.1112** | -87.9257 | 15.243 (top-ups 83.24) | -88.357 | 2 | 0 |
| `m1_random` | 871 / 98 / 112 | 870 | 25% | +0.2571 | -0.2149 | **-0.0988** | -85.9794 | 15.864 (top-ups 82.11) | -86.405 | 1 | 0 |

- Exit reasons: {'take_profit': 416, 'stop_loss': 1086, 'no_volume_15m': 159}
- Sells priced by the verified curve formula because Jupiter had no route: 674
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.425, m1_random +6.131
- Circuit breakers fired: 82
- Stream gaps logged: 92012

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
