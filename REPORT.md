# Paper bot check-in (2026-11-26 00:55 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 1074 / 185 / 21 | 1074 | 23% | +0.2812 | -0.2154 | **-0.1003** | -107.6883 | 9.430 (top-ups 97.55) | -108.486 | 0 | 0 |
| `m1_random` | 1053 / 114 / 118 | 1051 | 24% | +0.2532 | -0.2120 | **-0.1000** | -105.1093 | 10.855 (top-ups 96.30) | -105.598 | 2 | 0 |

- Exit reasons: {'take_profit': 513, 'stop_loss': 1392, 'no_volume_15m': 219, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 919
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +3.155, m1_random +6.805
- Circuit breakers fired: 101
- Stream gaps logged: 112762

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.

## Since amendment B2 (2026-11-24 00:00 UTC, exits from the price paid) — the comparison that counts now

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 92 / 13 / 0 | 92 | 25% | +0.3422 | -0.2215 | **-0.0806** | -7.4167 | 9.430 (top-ups 97.55) | -9.309 | 0 | 0 |
| `m1_random` | 55 / 4 / 3 | 53 | 17% | +0.2505 | -0.1879 | **-0.1135** | -6.0155 | 10.855 (top-ups 96.30) | -6.074 | 2 | 0 |

- Exit reasons: {'stop_loss': 102, 'take_profit': 25, 'no_volume_15m': 18}
- Sells priced by the verified curve formula because Jupiter had no route: 79
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.269, m1_random +0.179
- Circuit breakers fired: 5
- Stream gaps logged: 8798

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
