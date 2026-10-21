# Paper bot check-in (2026-10-21 01:22 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now | Max drawdown | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 346 / 52 / 6 | 344 | 25% | +0.2744 | -0.2179 | **-0.0948** | -32.6241 | 13.060 (top-ups 25.51) | -161.2% | 2 | 0 |
| `m1_random` | 278 / 33 / 32 | 278 | 21% | +0.2608 | -0.2128 | **-0.1140** | -31.6859 | 14.008 (top-ups 25.42) | -156.6% | 0 | 0 |

- Exit reasons: {'take_profit': 154, 'stop_loss': 415, 'no_volume_15m': 53}
- Sells priced by the verified curve formula because Jupiter had no route: 209
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.248, m1_random +2.526
- Circuit breakers fired: 28
- Stream gaps logged: 23008

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
