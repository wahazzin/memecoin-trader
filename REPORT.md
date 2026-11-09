# Paper bot check-in (2026-11-09 00:43 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 626 / 102 / 17 | 626 | 23% | +0.2621 | -0.2193 | **-0.1093** | -68.4350 | 19.874 (top-ups 68.54) | -69.032 | 0 | 0 |
| `m1_random` | 689 / 80 / 89 | 689 | 24% | +0.2522 | -0.2104 | **-0.0990** | -68.1806 | 19.650 (top-ups 68.02) | -68.530 | 0 | 0 |

- Exit reasons: {'take_profit': 321, 'stop_loss': 863, 'no_volume_15m': 131}
- Sells priced by the verified curve formula because Jupiter had no route: 514
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.146, m1_random +4.831
- Circuit breakers fired: 66
- Stream gaps logged: 77350

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
