# Paper bot check-in (2026-10-15 01:05 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 202 / 27 / 1 | 201 | 23% | +0.2776 | -0.2090 | **-0.0952** | -19.1428 | 14.857 (top-ups 13.81) | -94.9% | 1 | 0 |
| `m1_random` | 154 / 20 / 21 | 154 | 21% | +0.2383 | -0.2045 | **-0.1096** | -16.8790 | 17.178 (top-ups 14.10) | -87.1% | 0 | 0 |

- Exit reasons: {'take_profit': 82, 'stop_loss': 233, 'no_volume_15m': 40}
- Sells priced by the verified curve formula because Jupiter had no route: 124
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.707, m1_random +1.490
- Circuit breakers fired: 16
- Stream gaps logged: 7554

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
