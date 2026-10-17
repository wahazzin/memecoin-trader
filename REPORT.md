# Paper bot check-in (2026-10-17 02:08 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 263 / 35 / 3 | 263 | 27% | +0.2870 | -0.2159 | **-0.0820** | -21.5752 | 12.179 (top-ups 13.81) | -113.0% | 0 | 0 |
| `m1_random` | 204 / 26 / 24 | 204 | 23% | +0.2409 | -0.2125 | **-0.1103** | -22.4971 | 11.543 (top-ups 14.10) | -112.7% | 0 | 0 |

- Exit reasons: {'take_profit': 123, 'stop_loss': 301, 'no_volume_15m': 43}
- Sells priced by the verified curve formula because Jupiter had no route: 155
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.984, m1_random +1.970
- Circuit breakers fired: 20
- Stream gaps logged: 15314

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
