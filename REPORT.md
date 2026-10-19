# Paper bot check-in (2026-10-19 01:06 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 304 / 45 / 5 | 303 | 25% | +0.2906 | -0.2206 | **-0.0924** | -27.9922 | 17.327 (top-ups 25.51) | -140.2% | 1 | 0 |
| `m1_random` | 223 / 28 / 27 | 222 | 21% | +0.2409 | -0.2112 | **-0.1176** | -26.0983 | 19.315 (top-ups 25.42) | -130.3% | 1 | 0 |

- Exit reasons: {'take_profit': 130, 'stop_loss': 346, 'no_volume_15m': 49}
- Sells priced by the verified curve formula because Jupiter had no route: 176
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.142, m1_random +2.051
- Circuit breakers fired: 24
- Stream gaps logged: 18225

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
