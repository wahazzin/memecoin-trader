# Paper bot check-in (2026-10-16 01:24 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 230 / 29 / 2 | 229 | 24% | +0.2948 | -0.2142 | **-0.0897** | -20.5490 | 13.664 (top-ups 13.81) | -101.4% | 1 | 0 |
| `m1_random` | 178 / 23 / 24 | 178 | 21% | +0.2383 | -0.2084 | **-0.1131** | -20.1274 | 13.922 (top-ups 14.10) | -101.5% | 0 | 0 |

- Exit reasons: {'take_profit': 99, 'stop_loss': 267, 'no_volume_15m': 41}
- Sells priced by the verified curve formula because Jupiter had no route: 138
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.832, m1_random +1.589
- Circuit breakers fired: 18
- Stream gaps logged: 9164

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
