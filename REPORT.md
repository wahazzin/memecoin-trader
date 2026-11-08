# Paper bot check-in (2026-11-08 02:40 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 625 / 101 / 17 | 625 | 23% | +0.2621 | -0.2195 | **-0.1093** | -68.3108 | 5.688 (top-ups 54.23) | -68.906 | 0 | 0 |
| `m1_random` | 684 / 80 / 89 | 684 | 24% | +0.2522 | -0.2103 | **-0.0981** | -67.0998 | 7.012 (top-ups 53.97) | -67.512 | 0 | 0 |

- Exit reasons: {'take_profit': 321, 'stop_loss': 859, 'no_volume_15m': 129}
- Sells priced by the verified curve formula because Jupiter had no route: 509
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.146, m1_random +4.829
- Circuit breakers fired: 65
- Stream gaps logged: 76741

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
