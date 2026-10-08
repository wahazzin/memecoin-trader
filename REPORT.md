# Paper bot check-in (2026-10-08 00:29 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 76 / 9 / 0 | 75 | 24% | +0.3509 | -0.1994 | **-0.0674** | -5.0517 | 14.924 | -26.7% | 1 | 0 |
| `m1_random` | 26 / 5 / 5 | 26 | 15% | +0.2307 | -0.2202 | **-0.1508** | -3.9216 | 16.066 | -20.3% | 0 | 0 |

- Exit reasons: {'take_profit': 27, 'stop_loss': 56, 'no_volume_15m': 18}
- Sells priced by the verified curve formula because Jupiter had no route: 50
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.331, m1_random +0.276
- Circuit breakers fired: 2
- Stream gaps logged: 33

Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
