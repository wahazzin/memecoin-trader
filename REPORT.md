# Paper bot check-in (2026-10-14 04:32 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 176 / 22 / 1 | 176 | 23% | +0.2893 | -0.2097 | **-0.0963** | -16.9428 | 16.812 (top-ups 13.81) | -85.3% | 0 | 0 |
| `m1_random` | 131 / 18 / 19 | 131 | 19% | +0.2400 | -0.2055 | **-0.1205** | -15.7842 | 18.331 (top-ups 14.10) | -79.7% | 0 | 0 |

- Exit reasons: {'take_profit': 67, 'stop_loss': 203, 'no_volume_15m': 37}
- Sells priced by the verified curve formula because Jupiter had no route: 114
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.632, m1_random +1.076
- Circuit breakers fired: 15
- Stream gaps logged: 6415

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
