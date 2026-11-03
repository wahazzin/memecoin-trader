# Paper bot check-in (2026-11-03 01:13 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 549 / 84 / 15 | 547 | 23% | +0.2704 | -0.2185 | **-0.1068** | -58.4127 | 15.820 (top-ups 54.23) | -58.774 | 2 | 0 |
| `m1_random` | 527 / 55 / 57 | 526 | 23% | +0.2585 | -0.2190 | **-0.1092** | -57.4289 | 16.395 (top-ups 53.97) | -57.733 | 1 | 0 |

- Exit reasons: {'take_profit': 265, 'stop_loss': 714, 'no_volume_15m': 94}
- Sells priced by the verified curve formula because Jupiter had no route: 387
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.055, m1_random +3.997
- Circuit breakers fired: 54
- Stream gaps logged: 65773

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
