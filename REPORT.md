# Paper bot check-in (2026-11-17 00:44 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 783 / 136 / 21 | 781 | 23% | +0.2604 | -0.2209 | **-0.1112** | -86.8684 | 16.186 (top-ups 83.24) | -87.552 | 2 | 0 |
| `m1_random` | 869 / 98 / 112 | 869 | 25% | +0.2571 | -0.2148 | **-0.0986** | -85.6557 | 16.212 (top-ups 82.11) | -86.057 | 0 | 0 |

- Exit reasons: {'take_profit': 414, 'stop_loss': 1079, 'no_volume_15m': 157}
- Sells priced by the verified curve formula because Jupiter had no route: 668
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.406, m1_random +6.131
- Circuit breakers fired: 82
- Stream gaps logged: 91995

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
