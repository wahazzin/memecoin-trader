# Paper bot check-in (2026-10-17 01:17 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 253 / 33 / 3 | 252 | 25% | +0.2924 | -0.2156 | **-0.0866** | -21.8179 | 11.882 (top-ups 13.81) | -113.0% | 1 | 0 |
| `m1_random` | 199 / 26 / 24 | 199 | 23% | +0.2409 | -0.2109 | **-0.1065** | -21.1893 | 12.851 (top-ups 14.10) | -111.5% | 0 | 0 |

- Exit reasons: {'take_profit': 116, 'stop_loss': 292, 'no_volume_15m': 43}
- Sells priced by the verified curve formula because Jupiter had no route: 149
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.982, m1_random +1.936
- Circuit breakers fired: 20
- Stream gaps logged: 15210

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
