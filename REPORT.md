# Paper bot check-in (2026-11-17 00:33 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 779 / 134 / 21 | 779 | 23% | +0.2608 | -0.2210 | **-0.1115** | -86.8847 | 16.047 (top-ups 83.24) | -87.552 | 0 | 0 |
| `m1_random` | 869 / 98 / 112 | 869 | 25% | +0.2571 | -0.2148 | **-0.0986** | -85.6557 | 16.212 (top-ups 82.11) | -86.057 | 0 | 0 |

- Exit reasons: {'take_profit': 414, 'stop_loss': 1077, 'no_volume_15m': 157}
- Sells priced by the verified curve formula because Jupiter had no route: 667
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.371, m1_random +6.131
- Circuit breakers fired: 82
- Stream gaps logged: 91984

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
