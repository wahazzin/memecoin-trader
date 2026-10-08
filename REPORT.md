# Paper bot check-in (2026-10-08 00:34 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 79 / 9 / 0 | 79 | 23% | +0.3509 | -0.2008 | **-0.0751** | -5.9337 | 14.080 | -30.9% | 0 | 0 |
| `m1_random` | 30 / 5 / 5 | 28 | 14% | +0.2307 | -0.2277 | **-0.1622** | -4.5424 | 15.446 | -23.4% | 2 | 0 |

- Exit reasons: {'take_profit': 27, 'stop_loss': 62, 'no_volume_15m': 18}
- Sells priced by the verified curve formula because Jupiter had no route: 51
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.332, m1_random +0.278
- Circuit breakers fired: 3
- Stream gaps logged: 34

Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
