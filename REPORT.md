# Paper bot check-in (2026-11-12 01:10 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 693 / 117 / 20 | 693 | 23% | +0.2581 | -0.2191 | **-0.1117** | -77.4082 | 10.871 (top-ups 68.54) | -78.120 | 0 | 0 |
| `m1_random` | 773 / 86 / 110 | 773 | 24% | +0.2504 | -0.2123 | **-0.0992** | -76.6862 | 11.124 (top-ups 68.02) | -77.056 | 0 | 0 |

- Exit reasons: {'take_profit': 363, 'stop_loss': 961, 'no_volume_15m': 142}
- Sells priced by the verified curve formula because Jupiter had no route: 591
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.204, m1_random +5.268
- Circuit breakers fired: 72
- Stream gaps logged: 82110

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
