# Paper bot check-in (2026-11-08 02:19 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 625 / 101 / 17 | 625 | 23% | +0.2621 | -0.2195 | **-0.1093** | -68.3108 | 5.688 (top-ups 54.23) | -68.906 | 0 | 0 |
| `m1_random` | 683 / 80 / 89 | 682 | 24% | +0.2522 | -0.2105 | **-0.0979** | -66.7438 | 6.616 (top-ups 53.97) | -67.512 | 1 | 0 |

- Exit reasons: {'take_profit': 321, 'stop_loss': 858, 'no_volume_15m': 128}
- Sells priced by the verified curve formula because Jupiter had no route: 508
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.146, m1_random +4.817
- Circuit breakers fired: 65
- Stream gaps logged: 76735

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
