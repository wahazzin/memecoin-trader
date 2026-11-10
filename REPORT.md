# Paper bot check-in (2026-11-10 00:37 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 662 / 106 / 17 | 662 | 23% | +0.2613 | -0.2190 | **-0.1087** | -71.9746 | 16.668 (top-ups 68.54) | -72.238 | 0 | 0 |
| `m1_random` | 709 / 83 / 99 | 708 | 24% | +0.2517 | -0.2103 | **-0.1000** | -70.8148 | 17.042 (top-ups 68.02) | -71.457 | 1 | 0 |

- Exit reasons: {'take_profit': 337, 'stop_loss': 897, 'no_volume_15m': 136}
- Sells priced by the verified curve formula because Jupiter had no route: 544
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.182, m1_random +4.858
- Circuit breakers fired: 68
- Stream gaps logged: 79232

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
