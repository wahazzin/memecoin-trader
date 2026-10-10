# Paper bot check-in (2026-10-10 00:02 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 98 / 12 / 0 | 98 | 22% | +0.3213 | -0.2125 | **-0.0927** | -9.0820 | 10.628 | -47.8% | 0 | 0 |
| `m1_random` | 52 / 8 / 8 | 52 | 12% | +0.1912 | -0.2180 | **-0.1708** | -8.8831 | 11.097 | -44.9% | 0 | 0 |

- Exit reasons: {'take_profit': 33, 'stop_loss': 93, 'no_volume_15m': 24}
- Sells priced by the verified curve formula because Jupiter had no route: 70
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.340, m1_random +0.546
- Circuit breakers fired: 6
- Stream gaps logged: 2007

Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
