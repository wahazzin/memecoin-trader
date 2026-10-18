# Paper bot check-in (2026-10-18 00:07 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 279 / 40 / 4 | 279 | 26% | +0.2818 | -0.2179 | **-0.0890** | -24.8240 | 9.283 (top-ups 13.81) | -122.2% | 0 | 0 |
| `m1_random` | 211 / 27 / 26 | 211 | 22% | +0.2409 | -0.2114 | **-0.1128** | -23.7948 | 10.244 (top-ups 14.10) | -119.1% | 0 | 0 |

- Exit reasons: {'take_profit': 127, 'stop_loss': 316, 'no_volume_15m': 47}
- Sells priced by the verified curve formula because Jupiter had no route: 166
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.022, m1_random +2.038
- Circuit breakers fired: 22
- Stream gaps logged: 16714

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
