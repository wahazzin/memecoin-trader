# Paper bot check-in (2026-10-30 00:32 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 468 / 67 / 12 | 467 | 24% | +0.2670 | -0.2237 | **-0.1081** | -50.4819 | 9.231 (top-ups 39.90) | -51.032 | 1 | 0 |
| `m1_random` | 436 / 48 / 41 | 436 | 22% | +0.2439 | -0.2163 | **-0.1129** | -49.2270 | 10.289 (top-ups 39.64) | -49.862 | 0 | 0 |

- Exit reasons: {'take_profit': 217, 'stop_loss': 604, 'no_volume_15m': 82}
- Sells priced by the verified curve formula because Jupiter had no route: 319
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.787, m1_random +3.390
- Circuit breakers fired: 46
- Stream gaps logged: 57580

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
