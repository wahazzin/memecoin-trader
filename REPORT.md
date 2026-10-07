# Paper bot check-in (2026-10-07 23:28 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 49 / 7 / 0 | 49 | 20% | +0.4392 | -0.1915 | **-0.0628** | -3.0775 | 16.904 | -17.0% | 0 | 0 |
| `m1_random` | 23 / 2 / 4 | 20 | 15% | +0.1696 | -0.2203 | **-0.1618** | -3.2369 | 17.264 | -14.4% | 3 | 0 |

- Exit reasons: {'take_profit': 16, 'stop_loss': 38, 'no_volume_15m': 15}
- Sells priced by the verified curve formula because Jupiter had no route: 32
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.192, m1_random +0.124
- Circuit breakers fired: 1
- Stream gaps logged: 17

Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
