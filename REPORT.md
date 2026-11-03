# Paper bot check-in (2026-11-03 01:33 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 551 / 84 / 15 | 551 | 23% | +0.2679 | -0.2175 | **-0.1056** | -58.2111 | 15.824 (top-ups 54.23) | -58.792 | 0 | 0 |
| `m1_random` | 528 / 56 / 57 | 528 | 23% | +0.2585 | -0.2183 | **-0.1091** | -57.5869 | 16.235 (top-ups 53.97) | -57.893 | 0 | 0 |

- Exit reasons: {'take_profit': 267, 'stop_loss': 715, 'no_volume_15m': 97}
- Sells priced by the verified curve formula because Jupiter had no route: 392
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.055, m1_random +3.997
- Circuit breakers fired: 54
- Stream gaps logged: 65834

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
