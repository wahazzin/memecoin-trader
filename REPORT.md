# Paper bot check-in (2026-11-18 01:28 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 815 / 137 / 21 | 815 | 22% | +0.2587 | -0.2190 | **-0.1117** | -91.0354 | 11.886 (top-ups 83.24) | -91.717 | 0 | 0 |
| `m1_random` | 904 / 104 / 113 | 904 | 25% | +0.2550 | -0.2134 | **-0.0973** | -87.9817 | 13.872 (top-ups 82.11) | -88.555 | 0 | 0 |

- Exit reasons: {'take_profit': 428, 'stop_loss': 1123, 'no_volume_15m': 168}
- Sells priced by the verified curve formula because Jupiter had no route: 704
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.470, m1_random +6.333
- Circuit breakers fired: 85
- Stream gaps logged: 93401

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
