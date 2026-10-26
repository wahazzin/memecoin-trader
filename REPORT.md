# Paper bot check-in (2026-10-26 20:46 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 407 / 59 / 9 | 407 | 24% | +0.2657 | -0.2234 | **-0.1056** | -42.9875 | 16.765 (top-ups 39.90) | -43.499 | 0 | 0 |
| `m1_random` | 358 / 41 / 38 | 358 | 22% | +0.2395 | -0.2174 | **-0.1192** | -42.6575 | 16.887 (top-ups 39.64) | -42.910 | 0 | 0 |

- Exit reasons: {'take_profit': 189, 'stop_loss': 513, 'no_volume_15m': 63}
- Sells priced by the verified curve formula because Jupiter had no route: 258
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +1.462, m1_random +3.199
- Circuit breakers fired: 40
- Stream gaps logged: 46336

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
