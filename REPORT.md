# Paper bot check-in (2026-11-07 00:19 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 600 / 96 / 16 | 600 | 22% | +0.2673 | -0.2190 | **-0.1104** | -66.2302 | 7.781 (top-ups 54.23) | -66.813 | 0 | 0 |
| `m1_random` | 665 / 76 / 82 | 665 | 24% | +0.2550 | -0.2111 | **-0.0982** | -65.3152 | 8.469 (top-ups 53.97) | -65.658 | 0 | 0 |

- Exit reasons: {'take_profit': 313, 'stop_loss': 830, 'no_volume_15m': 122}
- Sells priced by the verified curve formula because Jupiter had no route: 480
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.082, m1_random +4.767
- Circuit breakers fired: 62
- Stream gaps logged: 75754

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
