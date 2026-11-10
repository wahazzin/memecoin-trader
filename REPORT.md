# Paper bot check-in (2026-11-10 01:09 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 673 / 110 / 19 | 672 | 23% | +0.2613 | -0.2193 | **-0.1106** | -74.3033 | 13.965 (top-ups 68.54) | -74.941 | 1 | 0 |
| `m1_random` | 709 / 83 / 99 | 709 | 24% | +0.2514 | -0.2103 | **-0.0996** | -70.6174 | 17.208 (top-ups 68.02) | -71.457 | 0 | 0 |

- Exit reasons: {'take_profit': 340, 'stop_loss': 903, 'no_volume_15m': 138}
- Sells priced by the verified curve formula because Jupiter had no route: 552
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.191, m1_random +4.858
- Circuit breakers fired: 69
- Stream gaps logged: 79234

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
