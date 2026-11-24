# Paper bot check-in (2026-11-24 00:17 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 1006 / 179 / 21 | 1002 | 23% | +0.2846 | -0.2151 | **-0.0984** | -98.5767 | 18.673 (top-ups 97.55) | -101.034 | 4 | 0 |
| `m1_random` | 1000 / 110 / 116 | 998 | 24% | +0.2533 | -0.2134 | **-0.0993** | -99.0938 | 16.875 (top-ups 96.30) | -99.578 | 2 | 0 |

- Exit reasons: {'take_profit': 493, 'stop_loss': 1305, 'no_volume_15m': 201, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 855
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.911, m1_random +6.627
- Circuit breakers fired: 96
- Stream gaps logged: 104017

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.

## Since amendment B2 (2026-11-24 00:00 UTC, exits from the price paid) — the comparison that counts now

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 24 / 7 / 0 | 20 | 40% | +0.5569 | -0.2300 | **+0.0847** | +1.6949 | 18.673 (top-ups 97.55) | -0.538 | 4 | 0 |
| `m1_random` | 2 / 0 / 1 | 0 | — | +0.0000 | +0.0000 | **—** | +0.0000 | 16.875 (top-ups 96.30) | -0.054 | 2 | 0 |

- Exit reasons: {'stop_loss': 15, 'take_profit': 5}
- Sells priced by the verified curve formula because Jupiter had no route: 15
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.025
- Circuit breakers fired: 0
- Stream gaps logged: 53

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
