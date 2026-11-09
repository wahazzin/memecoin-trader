# Paper bot check-in (2026-11-09 01:30 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 632 / 103 / 17 | 632 | 23% | +0.2603 | -0.2194 | **-0.1101** | -69.5836 | 18.724 (top-ups 68.54) | -70.182 | 0 | 0 |
| `m1_random` | 689 / 80 / 90 | 689 | 24% | +0.2522 | -0.2104 | **-0.0990** | -68.1806 | 19.650 (top-ups 68.02) | -68.530 | 0 | 0 |

- Exit reasons: {'take_profit': 323, 'stop_loss': 867, 'no_volume_15m': 131}
- Sells priced by the verified curve formula because Jupiter had no route: 516
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.146, m1_random +4.831
- Circuit breakers fired: 66
- Stream gaps logged: 77381

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
