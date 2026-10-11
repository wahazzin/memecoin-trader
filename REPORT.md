# Paper bot check-in (2026-10-11 00:26 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 112 / 15 / 0 | 111 | 23% | +0.3144 | -0.2158 | **-0.0964** | -10.6997 | 8.993 | -57.0% | 1 | 0 |
| `m1_random` | 63 / 10 / 10 | 63 | 13% | +0.2107 | -0.2128 | **-0.1590** | -10.0195 | 9.958 | -50.6% | 0 | 0 |

- Exit reasons: {'take_profit': 39, 'stop_loss': 109, 'no_volume_15m': 26}
- Sells priced by the verified curve formula because Jupiter had no route: 79
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.364, m1_random +0.607
- Circuit breakers fired: 8
- Stream gaps logged: 2588

Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
