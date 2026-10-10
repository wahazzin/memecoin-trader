# Paper bot check-in (2026-10-10 17:32 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 104 / 15 / 0 | 104 | 22% | +0.3133 | -0.2144 | **-0.0977** | -10.1616 | 9.796 | -51.9% | 0 | 0 |
| `m1_random` | 62 / 9 / 8 | 62 | 13% | +0.2107 | -0.2142 | **-0.1594** | -9.8835 | 10.095 | -49.9% | 0 | 0 |

- Exit reasons: {'take_profit': 37, 'stop_loss': 103, 'no_volume_15m': 26}
- Sells priced by the verified curve formula because Jupiter had no route: 76
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.362, m1_random +0.607
- Circuit breakers fired: 8
- Stream gaps logged: 2377

Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
