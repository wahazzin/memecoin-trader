# Paper bot check-in (2026-11-26 00:18 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 1074 / 185 / 21 | 1073 | 23% | +0.2816 | -0.2154 | **-0.1005** | -107.8606 | 9.426 (top-ups 97.55) | -108.486 | 1 | 0 |
| `m1_random` | 1045 / 113 / 116 | 1044 | 24% | +0.2532 | -0.2118 | **-0.0992** | -103.5201 | 12.470 (top-ups 96.30) | -104.615 | 1 | 0 |

- Exit reasons: {'take_profit': 513, 'stop_loss': 1386, 'no_volume_15m': 217, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 915
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +3.155, m1_random +6.801
- Circuit breakers fired: 101
- Stream gaps logged: 112638

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.

## Since amendment B2 (2026-11-24 00:00 UTC, exits from the price paid) — the comparison that counts now

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 92 / 13 / 0 | 91 | 24% | +0.3499 | -0.2215 | **-0.0834** | -7.5890 | 9.426 (top-ups 97.55) | -9.309 | 1 | 0 |
| `m1_random` | 47 / 3 / 1 | 46 | 20% | +0.2505 | -0.1806 | **-0.0962** | -4.4263 | 12.470 (top-ups 96.30) | -5.090 | 1 | 0 |

- Exit reasons: {'stop_loss': 96, 'take_profit': 25, 'no_volume_15m': 16}
- Sells priced by the verified curve formula because Jupiter had no route: 75
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.269, m1_random +0.174
- Circuit breakers fired: 5
- Stream gaps logged: 8674

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
