# Paper bot check-in (2026-10-15 00:40 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 193 / 27 / 1 | 192 | 23% | +0.2841 | -0.2100 | **-0.0942** | -18.0922 | 15.611 (top-ups 13.81) | -91.2% | 1 | 0 |
| `m1_random` | 150 / 20 / 21 | 150 | 21% | +0.2462 | -0.2049 | **-0.1117** | -16.7493 | 17.307 (top-ups 14.10) | -87.1% | 0 | 0 |

- Exit reasons: {'take_profit': 79, 'stop_loss': 225, 'no_volume_15m': 38}
- Sells priced by the verified curve formula because Jupiter had no route: 120
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.677, m1_random +1.404
- Circuit breakers fired: 16
- Stream gaps logged: 7519

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
