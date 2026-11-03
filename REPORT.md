# Paper bot check-in (2026-11-03 02:35 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 559 / 86 / 15 | 559 | 23% | +0.2677 | -0.2179 | **-0.1067** | -59.6432 | 14.389 (top-ups 54.23) | -60.205 | 0 | 0 |
| `m1_random` | 532 / 56 / 57 | 532 | 23% | +0.2585 | -0.2185 | **-0.1100** | -58.5428 | 15.279 (top-ups 53.97) | -58.848 | 0 | 0 |

- Exit reasons: {'take_profit': 269, 'stop_loss': 725, 'no_volume_15m': 97}
- Sells priced by the verified curve formula because Jupiter had no route: 399
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.069, m1_random +3.997
- Circuit breakers fired: 54
- Stream gaps logged: 65995

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
