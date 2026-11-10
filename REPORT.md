# Paper bot check-in (2026-11-10 00:22 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 656 / 106 / 17 | 656 | 23% | +0.2627 | -0.2178 | **-0.1072** | -70.3399 | 17.965 (top-ups 68.54) | -72.054 | 0 | 0 |
| `m1_random` | 708 / 83 / 99 | 708 | 24% | +0.2517 | -0.2103 | **-0.1000** | -70.8148 | 17.010 (top-ups 68.02) | -71.457 | 0 | 0 |

- Exit reasons: {'take_profit': 336, 'stop_loss': 892, 'no_volume_15m': 136}
- Sells priced by the verified curve formula because Jupiter had no route: 540
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.146, m1_random +4.858
- Circuit breakers fired: 68
- Stream gaps logged: 79225

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
