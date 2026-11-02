# Paper bot check-in (2026-11-02 03:38 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 536 / 81 / 14 | 536 | 23% | +0.2717 | -0.2171 | **-0.1049** | -56.2395 | 17.802 (top-ups 54.23) | -56.793 | 0 | 0 |
| `m1_random` | 509 / 53 / 56 | 509 | 23% | +0.2623 | -0.2184 | **-0.1088** | -55.3963 | 18.435 (top-ups 53.97) | -55.693 | 0 | 0 |

- Exit reasons: {'take_profit': 257, 'stop_loss': 694, 'no_volume_15m': 94}
- Sells priced by the verified curve formula because Jupiter had no route: 377
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.047, m1_random +3.938
- Circuit breakers fired: 52
- Stream gaps logged: 61720

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
