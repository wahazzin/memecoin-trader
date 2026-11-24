# Paper bot check-in (2026-11-24 00:28 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 1022 / 182 / 21 | 1016 | 23% | +0.2836 | -0.2144 | **-0.0987** | -100.3148 | 17.263 (top-ups 97.55) | -101.034 | 6 | 0 |
| `m1_random` | 1004 / 110 / 116 | 1003 | 24% | +0.2533 | -0.2132 | **-0.0997** | -100.0155 | 15.986 (top-ups 96.30) | -100.466 | 1 | 0 |

- Exit reasons: {'take_profit': 496, 'stop_loss': 1319, 'no_volume_15m': 203, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 866
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +2.911, m1_random +6.627
- Circuit breakers fired: 96
- Stream gaps logged: 104054

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.

## Since amendment B2 (2026-11-24 00:00 UTC, exits from the price paid) — the comparison that counts now

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 40 / 10 / 0 | 34 | 29% | +0.4778 | -0.2009 | **-0.0013** | -0.0431 | 17.263 (top-ups 97.55) | -1.471 | 6 | 0 |
| `m1_random` | 6 / 0 / 1 | 5 | 0% | +0.0000 | -0.1843 | **-0.1843** | -0.9217 | 15.986 (top-ups 96.30) | -0.942 | 2 | 0 |

- Exit reasons: {'stop_loss': 29, 'take_profit': 8, 'no_volume_15m': 2}
- Sells priced by the verified curve formula because Jupiter had no route: 26
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.025, m1_random +0.000
- Circuit breakers fired: 0
- Stream gaps logged: 90

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
