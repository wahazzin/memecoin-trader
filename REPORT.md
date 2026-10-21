# Paper bot check-in (2026-10-21 00:57 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 339 / 52 / 6 | 339 | 25% | +0.2757 | -0.2188 | **-0.0948** | -32.1443 | 13.436 (top-ups 25.51) | -159.3% | 0 | 0 |
| `m1_random` | 277 / 32 / 31 | 277 | 21% | +0.2608 | -0.2122 | **-0.1131** | -31.3333 | 14.009 (top-ups 25.42) | -156.6% | 0 | 0 |

- Exit reasons: {'take_profit': 153, 'stop_loss': 411, 'no_volume_15m': 52}
- Sells priced by the verified curve formula because Jupiter had no route: 206
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.244, m1_random +2.526
- Circuit breakers fired: 28
- Stream gaps logged: 22964

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
