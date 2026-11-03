# Paper bot check-in (2026-11-03 00:47 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 545 / 83 / 15 | 544 | 23% | +0.2713 | -0.2181 | **-0.1065** | -57.9576 | 16.073 (top-ups 54.23) | -58.740 | 1 | 0 |
| `m1_random` | 523 / 55 / 57 | 523 | 23% | +0.2585 | -0.2193 | **-0.1088** | -56.8952 | 16.848 (top-ups 53.97) | -57.280 | 0 | 0 |

- Exit reasons: {'take_profit': 263, 'stop_loss': 710, 'no_volume_15m': 94}
- Sells priced by the verified curve formula because Jupiter had no route: 383
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.055, m1_random +3.997
- Circuit breakers fired: 54
- Stream gaps logged: 65715

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
