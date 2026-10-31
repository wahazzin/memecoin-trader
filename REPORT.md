# Paper bot check-in (2026-10-31 01:20 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 482 / 71 / 14 | 482 | 23% | +0.2673 | -0.2209 | **-0.1065** | -51.3142 | 8.416 (top-ups 39.90) | -52.674 | 0 | 0 |
| `m1_random` | 456 / 49 / 44 | 456 | 22% | +0.2454 | -0.2178 | **-0.1142** | -52.0599 | 7.450 (top-ups 39.64) | -52.347 | 0 | 0 |

- Exit reasons: {'take_profit': 225, 'stop_loss': 628, 'no_volume_15m': 85}
- Sells priced by the verified curve formula because Jupiter had no route: 328
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.872, m1_random +3.457
- Circuit breakers fired: 48
- Stream gaps logged: 59022

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
