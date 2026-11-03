# Paper bot check-in (2026-11-03 00:57 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 546 / 83 / 15 | 546 | 23% | +0.2704 | -0.2182 | **-0.1063** | -58.0486 | 15.988 (top-ups 54.23) | -58.740 | 0 | 0 |
| `m1_random` | 525 / 55 / 57 | 525 | 23% | +0.2585 | -0.2188 | **-0.1088** | -57.1134 | 16.710 (top-ups 53.97) | -57.417 | 0 | 0 |

- Exit reasons: {'take_profit': 265, 'stop_loss': 712, 'no_volume_15m': 94}
- Sells priced by the verified curve formula because Jupiter had no route: 385
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.055, m1_random +3.997
- Circuit breakers fired: 54
- Stream gaps logged: 65730

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
