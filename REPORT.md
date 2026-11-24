# Paper bot check-in (2026-11-24 13:02 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 1044 / 183 / 21 | 1044 | 23% | +0.2817 | -0.2138 | **-0.0985** | -102.8363 | 14.288 (top-ups 97.55) | -103.626 | 0 | 0 |
| `m1_random` | 1021 / 113 / 116 | 1021 | 24% | +0.2530 | -0.2127 | **-0.0996** | -101.6601 | 14.356 (top-ups 96.30) | -102.096 | 0 | 0 |

- Exit reasons: {'take_profit': 502, 'stop_loss': 1348, 'no_volume_15m': 214, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 892
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +3.045, m1_random +6.672
- Circuit breakers fired: 98
- Stream gaps logged: 105372

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.

## Since amendment B2 (2026-11-24 00:00 UTC, exits from the price paid) — the comparison that counts now

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 62 / 11 / 0 | 62 | 27% | +0.3706 | -0.1970 | **-0.0414** | -2.5646 | 14.288 (top-ups 97.55) | -4.449 | 0 | 0 |
| `m1_random` | 23 / 3 / 1 | 23 | 17% | +0.2343 | -0.1844 | **-0.1116** | -2.5664 | 14.356 (top-ups 96.30) | -2.572 | 0 | 0 |

- Exit reasons: {'stop_loss': 58, 'take_profit': 14, 'no_volume_15m': 13}
- Sells priced by the verified curve formula because Jupiter had no route: 52
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.159, m1_random +0.046
- Circuit breakers fired: 2
- Stream gaps logged: 1408

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
