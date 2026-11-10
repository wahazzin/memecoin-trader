# Paper bot check-in (2026-11-10 02:42 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 673 / 110 / 19 | 673 | 23% | +0.2613 | -0.2189 | **-0.1104** | -74.3221 | 13.971 (top-ups 68.54) | -74.941 | 0 | 0 |
| `m1_random` | 716 / 84 / 101 | 716 | 24% | +0.2517 | -0.2108 | **-0.0997** | -71.3760 | 16.444 (top-ups 68.02) | -72.050 | 0 | 0 |

- Exit reasons: {'take_profit': 342, 'stop_loss': 908, 'no_volume_15m': 139}
- Sells priced by the verified curve formula because Jupiter had no route: 555
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.191, m1_random +4.919
- Circuit breakers fired: 69
- Stream gaps logged: 79262

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
