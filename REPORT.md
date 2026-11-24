# Paper bot check-in (2026-11-24 00:12 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 998 / 175 / 21 | 997 | 23% | +0.2843 | -0.2150 | **-0.0988** | -98.5272 | 18.197 (top-ups 97.55) | -101.034 | 1 | 0 |
| `m1_random` | 999 / 110 / 115 | 998 | 24% | +0.2533 | -0.2134 | **-0.0993** | -99.0938 | 16.895 (top-ups 96.30) | -99.557 | 1 | 0 |

- Exit reasons: {'take_profit': 491, 'stop_loss': 1302, 'no_volume_15m': 201, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 850
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.911, m1_random +6.627
- Circuit breakers fired: 96
- Stream gaps logged: 104000

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.

## Since amendment B2 (2026-11-24 00:00 UTC, exits from the price paid) — the comparison that counts now

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 16 / 3 / 0 | 15 | 40% | +0.6363 | -0.2304 | **+0.1163** | +1.7445 | 18.197 (top-ups 97.55) | -0.538 | 1 | 0 |
| `m1_random` | 1 / 0 / 0 | 0 | — | +0.0000 | +0.0000 | **—** | +0.0000 | 16.895 (top-ups 96.30) | -0.033 | 1 | 0 |

- Exit reasons: {'stop_loss': 12, 'take_profit': 3}
- Sells priced by the verified curve formula because Jupiter had no route: 10
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.025
- Circuit breakers fired: 0
- Stream gaps logged: 36

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
