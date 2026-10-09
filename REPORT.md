# Paper bot check-in (2026-10-09 00:00 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 80 / 9 / 0 | 80 | 22% | +0.3509 | -0.1999 | **-0.0759** | -6.0753 | 14.041 | -31.0% | 0 | 0 |
| `m1_random` | 37 / 5 / 5 | 37 | 11% | +0.2307 | -0.2086 | **-0.1611** | -5.9606 | 14.027 | -30.4% | 0 | 0 |

- Exit reasons: {'take_profit': 27, 'stop_loss': 69, 'no_volume_15m': 21}
- Sells priced by the verified curve formula because Jupiter had no route: 54
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.332, m1_random +0.315
- Circuit breakers fired: 4
- Stream gaps logged: 743

Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
