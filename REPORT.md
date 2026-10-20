# Paper bot check-in (2026-10-20 00:38 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 313 / 47 / 6 | 313 | 25% | +0.2819 | -0.2200 | **-0.0933** | -29.2104 | 16.178 (top-ups 25.51) | -145.8% | 0 | 0 |
| `m1_random` | 251 / 30 / 29 | 251 | 20% | +0.2634 | -0.2126 | **-0.1159** | -29.0897 | 16.558 (top-ups 25.42) | -144.0% | 0 | 0 |

- Exit reasons: {'take_profit': 136, 'stop_loss': 377, 'no_volume_15m': 51}
- Sells priced by the verified curve formula because Jupiter had no route: 189
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.206, m1_random +2.145
- Circuit breakers fired: 26
- Stream gaps logged: 20666

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
