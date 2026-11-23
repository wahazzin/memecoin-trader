# Paper bot check-in (2026-11-23 01:38 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 941 / 167 / 21 | 939 | 23% | +0.2738 | -0.2162 | **-0.1050** | -98.6403 | 18.394 (top-ups 97.55) | -99.518 | 2 | 0 |
| `m1_random` | 980 / 109 / 114 | 978 | 25% | +0.2545 | -0.2138 | **-0.0989** | -96.6991 | 19.305 (top-ups 96.30) | -97.147 | 2 | 0 |

- Exit reasons: {'take_profit': 470, 'stop_loss': 1254, 'no_volume_15m': 192, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 815
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.753, m1_random +6.598
- Circuit breakers fired: 94
- Stream gaps logged: 102028

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
