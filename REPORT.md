# Paper bot check-in (2026-11-17 01:10 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 798 / 136 / 21 | 797 | 23% | +0.2598 | -0.2194 | **-0.1100** | -87.6708 | 15.238 (top-ups 83.24) | -88.361 | 1 | 0 |
| `m1_random` | 873 / 98 / 112 | 872 | 25% | +0.2571 | -0.2144 | **-0.0987** | -86.0312 | 15.811 (top-ups 82.11) | -86.458 | 1 | 0 |

- Exit reasons: {'take_profit': 418, 'stop_loss': 1092, 'no_volume_15m': 159}
- Sells priced by the verified curve formula because Jupiter had no route: 680
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.425, m1_random +6.131
- Circuit breakers fired: 82
- Stream gaps logged: 92021

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
