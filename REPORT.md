# Paper bot check-in (2026-10-08 00:24 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 68 / 9 / 0 | 68 | 25% | +0.3522 | -0.1964 | **-0.0592** | -4.0277 | 15.987 | -21.5% | 0 | 0 |
| `m1_random` | 25 / 4 / 5 | 25 | 16% | +0.2307 | -0.2246 | **-0.1518** | -3.7939 | 16.196 | -19.7% | 0 | 0 |

- Exit reasons: {'take_profit': 25, 'stop_loss': 50, 'no_volume_15m': 18}
- Sells priced by the verified curve formula because Jupiter had no route: 47
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.331, m1_random +0.276
- Circuit breakers fired: 2
- Stream gaps logged: 33

Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
