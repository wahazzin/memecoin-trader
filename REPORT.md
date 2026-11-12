# Paper bot check-in (2026-11-12 01:26 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 695 / 117 / 20 | 695 | 23% | +0.2570 | -0.2191 | **-0.1109** | -77.0732 | 11.117 (top-ups 68.54) | -78.120 | 0 | 0 |
| `m1_random` | 776 / 87 / 110 | 775 | 25% | +0.2546 | -0.2126 | **-0.0981** | -76.0194 | 10.809 (top-ups 68.02) | -77.371 | 1 | 0 |

- Exit reasons: {'take_profit': 366, 'stop_loss': 962, 'no_volume_15m': 142}
- Sells priced by the verified curve formula because Jupiter had no route: 594
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.204, m1_random +5.292
- Circuit breakers fired: 72
- Stream gaps logged: 82129

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
