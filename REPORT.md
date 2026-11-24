# Paper bot check-in (2026-11-24 00:07 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 991 / 174 / 21 | 990 | 23% | +0.2846 | -0.2149 | **-0.0994** | -98.3901 | 18.735 (top-ups 97.55) | -101.034 | 1 | 0 |
| `m1_random` | 999 / 110 / 115 | 998 | 24% | +0.2533 | -0.2134 | **-0.0993** | -99.0938 | 16.895 (top-ups 96.30) | -99.557 | 1 | 0 |

- Exit reasons: {'take_profit': 490, 'stop_loss': 1296, 'no_volume_15m': 201, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 847
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.911, m1_random +6.627
- Circuit breakers fired: 96
- Stream gaps logged: 103987

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.

## Since amendment B2 (2026-11-24 00:00 UTC, exits from the price paid) — the comparison that counts now

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 9 / 2 / 0 | 8 | 38% | +1.0100 | -0.2297 | **+0.2352** | +1.8816 | 18.735 (top-ups 97.55) | +0.000 | 1 | 0 |
| `m1_random` | 1 / 0 / 0 | 0 | — | +0.0000 | +0.0000 | **—** | +0.0000 | 16.895 (top-ups 96.30) | -0.033 | 1 | 0 |

- Exit reasons: {'stop_loss': 6, 'take_profit': 2}
- Sells priced by the verified curve formula because Jupiter had no route: 7
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.025
- Circuit breakers fired: 0
- Stream gaps logged: 23

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
