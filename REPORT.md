# Paper bot check-in (2026-10-30 04:30 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 474 / 69 / 13 | 474 | 23% | +0.2670 | -0.2223 | **-0.1087** | -51.5355 | 8.197 (top-ups 39.90) | -52.064 | 0 | 0 |
| `m1_random` | 445 / 48 / 43 | 445 | 23% | +0.2453 | -0.2167 | **-0.1119** | -49.7831 | 9.730 (top-ups 39.64) | -50.286 | 0 | 0 |

- Exit reasons: {'take_profit': 221, 'stop_loss': 614, 'no_volume_15m': 84}
- Sells priced by the verified curve formula because Jupiter had no route: 324
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.802, m1_random +3.393
- Circuit breakers fired: 47
- Stream gaps logged: 58180

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
