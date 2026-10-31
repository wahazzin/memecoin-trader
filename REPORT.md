# Paper bot check-in (2026-10-31 01:41 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 488 / 72 / 14 | 487 | 24% | +0.2634 | -0.2205 | **-0.1053** | -51.2620 | 8.262 (top-ups 39.90) | -52.674 | 1 | 0 |
| `m1_random` | 458 / 49 / 44 | 457 | 22% | +0.2454 | -0.2179 | **-0.1145** | -52.3153 | 6.954 (top-ups 39.64) | -52.843 | 1 | 0 |

- Exit reasons: {'take_profit': 229, 'stop_loss': 630, 'no_volume_15m': 85}
- Sells priced by the verified curve formula because Jupiter had no route: 328
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.939, m1_random +3.457
- Circuit breakers fired: 48
- Stream gaps logged: 59046

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
