# Paper bot check-in (2026-11-07 00:50 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 604 / 97 / 16 | 604 | 22% | +0.2658 | -0.2191 | **-0.1107** | -66.8837 | 7.384 (top-ups 54.23) | -67.240 | 0 | 0 |
| `m1_random` | 666 / 76 / 82 | 666 | 24% | +0.2544 | -0.2111 | **-0.0979** | -65.1693 | 8.615 (top-ups 53.97) | -65.658 | 0 | 0 |

- Exit reasons: {'take_profit': 315, 'stop_loss': 833, 'no_volume_15m': 122}
- Sells priced by the verified curve formula because Jupiter had no route: 484
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.082, m1_random +4.767
- Circuit breakers fired: 62
- Stream gaps logged: 75782

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
