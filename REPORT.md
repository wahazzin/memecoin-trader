# Paper bot check-in (2026-11-07 00:40 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 603 / 97 / 16 | 602 | 22% | +0.2658 | -0.2194 | **-0.1106** | -66.5933 | 8.000 (top-ups 54.23) | -67.240 | 1 | 0 |
| `m1_random` | 665 / 76 / 82 | 665 | 24% | +0.2550 | -0.2111 | **-0.0982** | -65.3152 | 8.469 (top-ups 53.97) | -65.658 | 0 | 0 |

- Exit reasons: {'take_profit': 314, 'stop_loss': 831, 'no_volume_15m': 122}
- Sells priced by the verified curve formula because Jupiter had no route: 482
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.082, m1_random +4.767
- Circuit breakers fired: 62
- Stream gaps logged: 75775

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
