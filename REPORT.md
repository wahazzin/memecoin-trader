# Paper bot check-in (2026-11-17 00:49 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 786 / 136 / 21 | 784 | 23% | +0.2597 | -0.2208 | **-0.1111** | -87.1192 | 16.152 (top-ups 83.24) | -87.552 | 2 | 0 |
| `m1_random` | 870 / 98 / 112 | 869 | 25% | +0.2571 | -0.2148 | **-0.0986** | -85.6557 | 16.212 (top-ups 82.11) | -86.057 | 1 | 0 |

- Exit reasons: {'take_profit': 414, 'stop_loss': 1082, 'no_volume_15m': 157}
- Sells priced by the verified curve formula because Jupiter had no route: 669
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.421, m1_random +6.131
- Circuit breakers fired: 82
- Stream gaps logged: 91999

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
