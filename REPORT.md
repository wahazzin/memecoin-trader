# Paper bot check-in (2026-11-02 03:33 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 536 / 81 / 14 | 536 | 23% | +0.2717 | -0.2171 | **-0.1049** | -56.2395 | 18.267 (top-ups 54.23) | -56.345 | 0 | 0 |
| `m1_random` | 507 / 53 / 56 | 507 | 23% | +0.2623 | -0.2193 | **-0.1091** | -55.3176 | 18.929 (top-ups 53.97) | -55.432 | 0 | 0 |

- Exit reasons: {'take_profit': 256, 'stop_loss': 693, 'no_volume_15m': 94}
- Sells priced by the verified curve formula because Jupiter had no route: 377
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.047, m1_random +3.938
- Circuit breakers fired: 52
- Stream gaps logged: 61717

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
