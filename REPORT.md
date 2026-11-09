# Paper bot check-in (2026-11-09 02:22 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 637 / 103 / 17 | 637 | 23% | +0.2589 | -0.2188 | **-0.1100** | -70.0987 | 18.209 (top-ups 68.54) | -70.760 | 0 | 0 |
| `m1_random` | 690 / 80 / 92 | 690 | 24% | +0.2522 | -0.2103 | **-0.0990** | -68.3346 | 19.496 (top-ups 68.02) | -68.684 | 0 | 0 |

- Exit reasons: {'take_profit': 323, 'stop_loss': 872, 'no_volume_15m': 132}
- Sells priced by the verified curve formula because Jupiter had no route: 520
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.146, m1_random +4.831
- Circuit breakers fired: 66
- Stream gaps logged: 77408

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
