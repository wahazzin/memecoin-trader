# Paper bot check-in (2026-11-03 00:05 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 540 / 81 / 14 | 540 | 23% | +0.2717 | -0.2178 | **-0.1063** | -57.3913 | 17.003 (top-ups 54.23) | -57.614 | 0 | 0 |
| `m1_random` | 521 / 54 / 57 | 521 | 23% | +0.2599 | -0.2191 | **-0.1087** | -56.6479 | 16.936 (top-ups 53.97) | -57.191 | 0 | 0 |

- Exit reasons: {'take_profit': 261, 'stop_loss': 706, 'no_volume_15m': 94}
- Sells priced by the verified curve formula because Jupiter had no route: 380
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.047, m1_random +3.997
- Circuit breakers fired: 54
- Stream gaps logged: 65550

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
