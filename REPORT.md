# Paper bot check-in (2026-11-08 01:12 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 620 / 100 / 17 | 620 | 23% | +0.2615 | -0.2200 | **-0.1097** | -68.0153 | 5.985 (top-ups 54.23) | -68.609 | 0 | 0 |
| `m1_random` | 681 / 80 / 88 | 681 | 24% | +0.2513 | -0.2105 | **-0.0986** | -67.1381 | 6.640 (top-ups 53.97) | -67.487 | 0 | 0 |

- Exit reasons: {'take_profit': 319, 'stop_loss': 854, 'no_volume_15m': 128}
- Sells priced by the verified curve formula because Jupiter had no route: 505
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.144, m1_random +4.817
- Circuit breakers fired: 64
- Stream gaps logged: 76700

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
