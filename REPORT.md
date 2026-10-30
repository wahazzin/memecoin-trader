# Paper bot check-in (2026-10-30 02:21 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 474 / 69 / 13 | 474 | 23% | +0.2670 | -0.2223 | **-0.1087** | -51.5355 | 8.197 (top-ups 39.90) | -52.064 | 0 | 0 |
| `m1_random` | 441 / 48 / 42 | 441 | 23% | +0.2455 | -0.2168 | **-0.1120** | -49.3863 | 10.128 (top-ups 39.64) | -49.997 | 0 | 0 |

- Exit reasons: {'take_profit': 220, 'stop_loss': 611, 'no_volume_15m': 84}
- Sells priced by the verified curve formula because Jupiter had no route: 324
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.802, m1_random +3.390
- Circuit breakers fired: 47
- Stream gaps logged: 57767

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
