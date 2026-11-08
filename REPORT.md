# Paper bot check-in (2026-11-08 00:15 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 608 / 99 / 17 | 607 | 22% | +0.2647 | -0.2194 | **-0.1110** | -67.3533 | 6.756 (top-ups 54.23) | -67.838 | 1 | 0 |
| `m1_random` | 679 / 78 / 85 | 679 | 24% | +0.2513 | -0.2111 | **-0.0987** | -67.0236 | 6.758 (top-ups 53.97) | -67.370 | 0 | 0 |

- Exit reasons: {'take_profit': 315, 'stop_loss': 847, 'no_volume_15m': 124}
- Sells priced by the verified curve formula because Jupiter had no route: 495
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.082, m1_random +4.817
- Circuit breakers fired: 64
- Stream gaps logged: 76681

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
