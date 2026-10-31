# Paper bot check-in (2026-10-31 00:29 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 478 / 70 / 13 | 478 | 23% | +0.2670 | -0.2211 | **-0.1088** | -52.0034 | 7.726 (top-ups 39.90) | -52.536 | 0 | 0 |
| `m1_random` | 454 / 49 / 43 | 454 | 22% | +0.2454 | -0.2176 | **-0.1136** | -51.5781 | 7.931 (top-ups 39.64) | -51.865 | 0 | 0 |

- Exit reasons: {'take_profit': 222, 'stop_loss': 625, 'no_volume_15m': 85}
- Sells priced by the verified curve formula because Jupiter had no route: 326
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.857, m1_random +3.457
- Circuit breakers fired: 48
- Stream gaps logged: 58896

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
