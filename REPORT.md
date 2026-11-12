# Paper bot check-in (2026-11-12 09:46 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 704 / 119 / 20 | 704 | 22% | +0.2570 | -0.2185 | **-0.1118** | -78.6830 | 9.593 (top-ups 68.54) | -79.313 | 0 | 0 |
| `m1_random` | 797 / 88 / 111 | 797 | 25% | +0.2599 | -0.2136 | **-0.0966** | -76.9611 | 10.843 (top-ups 68.02) | -77.371 | 0 | 0 |

- Exit reasons: {'take_profit': 374, 'stop_loss': 983, 'no_volume_15m': 144}
- Sells priced by the verified curve formula because Jupiter had no route: 605
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.204, m1_random +5.559
- Circuit breakers fired: 73
- Stream gaps logged: 82280

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
