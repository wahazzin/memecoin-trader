# Paper bot check-in (2026-11-08 00:35 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 614 / 99 / 17 | 613 | 23% | +0.2625 | -0.2195 | **-0.1094** | -67.0596 | 6.946 (top-ups 54.23) | -68.270 | 1 | 0 |
| `m1_random` | 680 / 79 / 85 | 680 | 24% | +0.2513 | -0.2108 | **-0.0987** | -67.0961 | 6.684 (top-ups 53.97) | -67.444 | 0 | 0 |

- Exit reasons: {'take_profit': 317, 'stop_loss': 850, 'no_volume_15m': 126}
- Sells priced by the verified curve formula because Jupiter had no route: 500
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.101, m1_random +4.817
- Circuit breakers fired: 64
- Stream gaps logged: 76693

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
