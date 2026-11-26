# Paper bot check-in (2026-11-26 01:26 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 1074 / 185 / 21 | 1074 | 23% | +0.2812 | -0.2154 | **-0.1003** | -107.6883 | 9.430 (top-ups 97.55) | -108.486 | 0 | 0 |
| `m1_random` | 1059 / 114 / 118 | 1059 | 24% | +0.2531 | -0.2112 | **-0.0998** | -105.6998 | 10.313 (top-ups 96.30) | -106.141 | 0 | 0 |

- Exit reasons: {'take_profit': 514, 'stop_loss': 1395, 'no_volume_15m': 223, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 924
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +3.155, m1_random +6.839
- Circuit breakers fired: 101
- Stream gaps logged: 112882

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.

## Since amendment B2 (2026-11-24 00:00 UTC, exits from the price paid) — the comparison that counts now

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 92 / 13 / 0 | 92 | 25% | +0.3422 | -0.2215 | **-0.0806** | -7.4167 | 9.430 (top-ups 97.55) | -9.309 | 0 | 0 |
| `m1_random` | 61 / 4 / 3 | 61 | 16% | +0.2484 | -0.1782 | **-0.1083** | -6.6060 | 10.313 (top-ups 96.30) | -6.617 | 0 | 0 |

- Exit reasons: {'stop_loss': 105, 'take_profit': 26, 'no_volume_15m': 22}
- Sells priced by the verified curve formula because Jupiter had no route: 84
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.269, m1_random +0.212
- Circuit breakers fired: 5
- Stream gaps logged: 8918

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
