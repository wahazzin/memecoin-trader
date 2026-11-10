# Paper bot check-in (2026-11-10 07:23 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 673 / 110 / 19 | 673 | 23% | +0.2613 | -0.2189 | **-0.1104** | -74.3221 | 13.971 (top-ups 68.54) | -74.941 | 0 | 0 |
| `m1_random` | 730 / 85 / 101 | 730 | 24% | +0.2493 | -0.2119 | **-0.1001** | -73.0721 | 14.744 (top-ups 68.02) | -73.559 | 0 | 0 |

- Exit reasons: {'take_profit': 347, 'stop_loss': 915, 'no_volume_15m': 141}
- Sells priced by the verified curve formula because Jupiter had no route: 565
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.191, m1_random +4.975
- Circuit breakers fired: 69
- Stream gaps logged: 79356

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
