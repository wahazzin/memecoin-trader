# Paper bot check-in (2026-11-08 01:58 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 624 / 101 / 17 | 623 | 23% | +0.2621 | -0.2194 | **-0.1089** | -67.8309 | 6.168 (top-ups 54.23) | -68.609 | 1 | 0 |
| `m1_random` | 681 / 80 / 89 | 681 | 24% | +0.2513 | -0.2105 | **-0.0986** | -67.1381 | 6.640 (top-ups 53.97) | -67.487 | 0 | 0 |

- Exit reasons: {'take_profit': 320, 'stop_loss': 856, 'no_volume_15m': 128}
- Sells priced by the verified curve formula because Jupiter had no route: 507
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.144, m1_random +4.817
- Circuit breakers fired: 64
- Stream gaps logged: 76714

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
