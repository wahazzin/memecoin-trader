# Paper bot check-in (2026-11-08 00:51 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 617 / 99 / 17 | 615 | 23% | +0.2631 | -0.2195 | **-0.1089** | -66.9524 | 7.057 (top-ups 54.23) | -68.270 | 2 | 0 |
| `m1_random` | 681 / 80 / 87 | 681 | 24% | +0.2513 | -0.2105 | **-0.0986** | -67.1381 | 6.640 (top-ups 53.97) | -67.487 | 0 | 0 |

- Exit reasons: {'take_profit': 318, 'stop_loss': 852, 'no_volume_15m': 126}
- Sells priced by the verified curve formula because Jupiter had no route: 502
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.101, m1_random +4.817
- Circuit breakers fired: 64
- Stream gaps logged: 76699

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
