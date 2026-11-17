# Paper bot check-in (2026-11-17 01:05 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 797 / 136 / 21 | 796 | 23% | +0.2598 | -0.2194 | **-0.1099** | -87.4475 | 15.457 (top-ups 83.24) | -88.357 | 1 | 0 |
| `m1_random` | 873 / 98 / 112 | 871 | 25% | +0.2571 | -0.2146 | **-0.0987** | -86.0004 | 15.843 (top-ups 82.11) | -86.426 | 2 | 0 |

- Exit reasons: {'take_profit': 418, 'stop_loss': 1090, 'no_volume_15m': 159}
- Sells priced by the verified curve formula because Jupiter had no route: 679
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.425, m1_random +6.131
- Circuit breakers fired: 82
- Stream gaps logged: 92015

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
