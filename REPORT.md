# Paper bot check-in (2026-11-25 00:34 UTC)

> PAPER ONLY. Fills = live Jupiter quotes (worse of two, 2 s apart) + measured costs (COST_FACTORS.md).

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 1064 / 184 / 21 | 1064 | 23% | +0.2816 | -0.2151 | **-0.0993** | -105.6922 | 11.591 (top-ups 97.55) | -106.321 | 0 | 0 |
| `m1_random` | 1031 / 113 / 116 | 1030 | 24% | +0.2530 | -0.2126 | **-0.1005** | -103.5360 | 12.817 (top-ups 96.30) | -103.635 | 1 | 0 |

- Exit reasons: {'take_profit': 507, 'stop_loss': 1371, 'no_volume_15m': 215, 'max_hold_60m': 1}
- Sells priced by the verified curve formula because Jupiter had no route: 903
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +3.142, m1_random +6.719
- Circuit breakers fired: 99
- Stream gaps logged: 109040

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.

## Since amendment B2 (2026-11-24 00:00 UTC, exits from the price paid) — the comparison that counts now

| Arm | Buys filled / failed / no route | Closed | Win rate | Avg win | Avg loss | **Expectancy / trade** | Total P&L (SOL) | Equity now (all top-ups so far) | Max drawdown (SOL, top-ups removed) | Open | Stuck |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `m1_pass` | 82 / 12 / 0 | 82 | 27% | +0.3499 | -0.2186 | **-0.0661** | -5.4205 | 11.591 (top-ups 97.55) | -7.144 | 0 | 0 |
| `m1_random` | 33 / 3 / 1 | 32 | 12% | +0.2343 | -0.1921 | **-0.1388** | -4.4423 | 12.817 (top-ups 96.30) | -4.111 | 1 | 0 |

- Exit reasons: {'stop_loss': 81, 'take_profit': 19, 'no_volume_15m': 14}
- Sells priced by the verified curve formula because Jupiter had no route: 63
- Delay sensitivity (sells only): SOL gained if sells had filled at the first quote instead of the worse one: m1_pass +0.256, m1_random +0.092
- Circuit breakers fired: 3
- Stream gaps logged: 5076

Equity now includes paper top-ups (BOT_SPEC B1); max drawdown is computed with top-ups removed.
Expectancy = win rate × avg win + loss rate × avg loss, per closed trade, in SOL after all costs (rule 6).
The test is `m1_pass` vs `m1_random` (same entry moment, checks vs no checks). See BOT_SPEC.md.
