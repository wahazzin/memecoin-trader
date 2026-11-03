# Paper bot check-in (2026-11-03 02:04 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 556 / 86 / 15 | 556 | 23% | +0.2677 | -0.2175 | **-0.1058** | -58.8415 | 15.383 (top-ups 54.23) | -59.212 | 0 | 0 |
| `m1_random` | 532 / 56 / 57 | 532 | 23% | +0.2585 | -0.2185 | **-0.1100** | -58.5428 | 15.423 (top-ups 53.97) | -58.704 | 0 | 0 |

- Exit reasons: {'take_profit': 268, 'stop_loss': 723, 'no_volume_15m': 97}
- Sells priced by the verified curve formula because Jupiter had no route: 398
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.055, m1_random +3.997
- Circuit breakers fired: 54
- Stream gaps logged: 65912

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
