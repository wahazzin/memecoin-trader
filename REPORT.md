# Paper bot check-in (2026-11-03 01:18 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 550 / 84 / 15 | 548 | 23% | +0.2704 | -0.2180 | **-0.1066** | -58.4309 | 15.802 (top-ups 54.23) | -58.792 | 2 | 0 |
| `m1_random` | 528 / 55 / 57 | 527 | 23% | +0.2585 | -0.2188 | **-0.1092** | -57.5687 | 16.397 (top-ups 53.97) | -57.733 | 1 | 0 |

- Exit reasons: {'take_profit': 266, 'stop_loss': 715, 'no_volume_15m': 94}
- Sells priced by the verified curve formula because Jupiter had no route: 388
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.055, m1_random +3.997
- Circuit breakers fired: 54
- Stream gaps logged: 65786

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
