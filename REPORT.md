# Paper bot check-in (2026-11-05 00:06 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 577 / 92 / 16 | 577 | 23% | +0.2672 | -0.2201 | **-0.1095** | -63.1657 | 11.541 (top-ups 54.23) | -63.054 | 0 | 0 |
| `m1_random` | 592 / 67 / 72 | 592 | 23% | +0.2562 | -0.2138 | **-0.1058** | -62.6341 | 11.867 (top-ups 53.97) | -62.260 | 0 | 0 |

- Exit reasons: {'take_profit': 287, 'stop_loss': 770, 'no_volume_15m': 112}
- Sells priced by the verified curve formula because Jupiter had no route: 441
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.082, m1_random +4.443
- Circuit breakers fired: 58
- Stream gaps logged: 71380

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
