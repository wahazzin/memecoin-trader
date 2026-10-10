# Paper bot check-in (2026-10-10 00:32 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 104 / 15 / 0 | 104 | 22% | +0.3133 | -0.2144 | **-0.0977** | -10.1616 | 9.796 | -51.9% | 0 | 0 |
| `m1_random` | 59 / 9 / 8 | 59 | 12% | +0.2192 | -0.2144 | **-0.1629** | -9.6132 | 10.366 | -48.6% | 0 | 0 |

- Exit reasons: {'take_profit': 36, 'stop_loss': 101, 'no_volume_15m': 26}
- Sells priced by the verified curve formula because Jupiter had no route: 76
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.362, m1_random +0.575
- Circuit breakers fired: 7
- Stream gaps logged: 2076

Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
