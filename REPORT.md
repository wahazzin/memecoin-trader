# Paper bot check-in (2026-11-12 01:42 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 701 / 119 / 20 | 700 | 23% | +0.2570 | -0.2189 | **-0.1115** | -78.0490 | 10.359 (top-ups 68.54) | -78.547 | 1 | 0 |
| `m1_random` | 776 / 87 / 110 | 776 | 24% | +0.2546 | -0.2128 | **-0.0984** | -76.3280 | 11.480 (top-ups 68.02) | -77.371 | 0 | 0 |

- Exit reasons: {'take_profit': 367, 'stop_loss': 967, 'no_volume_15m': 142}
- Sells priced by the verified curve formula because Jupiter had no route: 597
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.204, m1_random +5.292
- Circuit breakers fired: 72
- Stream gaps logged: 82149

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
