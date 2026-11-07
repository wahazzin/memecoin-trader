# Paper bot check-in (2026-11-07 01:37 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 606 / 98 / 16 | 606 | 22% | +0.2647 | -0.2194 | **-0.1108** | -67.1348 | 6.873 (top-ups 54.23) | -67.721 | 0 | 0 |
| `m1_random` | 666 / 76 / 83 | 666 | 24% | +0.2544 | -0.2111 | **-0.0979** | -65.1693 | 8.615 (top-ups 53.97) | -65.658 | 0 | 0 |

- Exit reasons: {'take_profit': 315, 'stop_loss': 835, 'no_volume_15m': 122}
- Sells priced by the verified curve formula because Jupiter had no route: 486
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.082, m1_random +4.767
- Circuit breakers fired: 63
- Stream gaps logged: 75821

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
