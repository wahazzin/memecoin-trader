# Paper bot check-in (2026-10-16 01:03 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 222 / 29 / 1 | 222 | 25% | +0.2948 | -0.2082 | **-0.0813** | -18.0478 | 15.691 (top-ups 13.81) | -101.4% | 0 | 0 |
| `m1_random` | 175 / 23 / 23 | 175 | 21% | +0.2374 | -0.2077 | **-0.1136** | -19.8793 | 14.170 (top-ups 14.10) | -101.5% | 0 | 0 |

- Exit reasons: {'take_profit': 97, 'stop_loss': 259, 'no_volume_15m': 41}
- Sells priced by the verified curve formula because Jupiter had no route: 136
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.812, m1_random +1.549
- Circuit breakers fired: 18
- Stream gaps logged: 9021

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
