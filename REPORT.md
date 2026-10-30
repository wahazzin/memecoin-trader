# Paper bot check-in (2026-10-30 00:53 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 473 / 69 / 13 | 472 | 23% | +0.2670 | -0.2227 | **-0.1085** | -51.2261 | 8.476 (top-ups 39.90) | -51.786 | 1 | 0 |
| `m1_random` | 438 / 48 / 41 | 438 | 23% | +0.2461 | -0.2171 | **-0.1124** | -49.2395 | 10.275 (top-ups 39.64) | -49.862 | 0 | 0 |

- Exit reasons: {'take_profit': 219, 'stop_loss': 608, 'no_volume_15m': 83}
- Sells priced by the verified curve formula because Jupiter had no route: 322
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.802, m1_random +3.390
- Circuit breakers fired: 46
- Stream gaps logged: 57641

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
