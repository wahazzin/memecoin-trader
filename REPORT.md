# Paper bot check-in (2026-10-31 01:46 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 492 / 72 / 14 | 490 | 24% | +0.2634 | -0.2215 | **-0.1067** | -52.2748 | 7.963 (top-ups 39.90) | -52.674 | 2 | 0 |
| `m1_random` | 458 / 49 / 44 | 457 | 22% | +0.2454 | -0.2179 | **-0.1145** | -52.3153 | 6.954 (top-ups 39.64) | -52.843 | 1 | 0 |

- Exit reasons: {'take_profit': 229, 'stop_loss': 633, 'no_volume_15m': 85}
- Sells priced by the verified curve formula because Jupiter had no route: 329
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.945, m1_random +3.457
- Circuit breakers fired: 49
- Stream gaps logged: 59059

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
