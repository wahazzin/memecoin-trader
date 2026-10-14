# Paper bot check-in (2026-10-14 01:04 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 153 / 21 / 1 | 152 | 23% | +0.2956 | -0.2095 | **-0.0932** | -14.1652 | 19.714 (top-ups 13.81) | -74.4% | 1 | 0 |
| `m1_random` | 114 / 13 / 16 | 114 | 20% | +0.2233 | -0.2059 | **-0.1193** | -13.5961 | 20.474 (top-ups 14.10) | -70.7% | 0 | 0 |

- Exit reasons: {'take_profit': 61, 'stop_loss': 168, 'no_volume_15m': 37}
- Sells priced by the verified curve formula because Jupiter had no route: 104
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.464, m1_random +0.918
- Circuit breakers fired: 14
- Stream gaps logged: 6276

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
