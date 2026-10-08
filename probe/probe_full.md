# Probe: open questions from pump.fun docs (2026-10-08 08:27 UTC)

## pump program, 120 s: 5383 txs, 3757 trades, kinds {'trade': 3757, 'amm_trade': 2, 'complete': 1, 'amm_create': 1, 'migrated': 1}
- quote mints: [('11111111', 3713), ('XspzcW1P', 23), ('Xsc9qvGR', 9), ('pumpCmXq', 3), ('2zMMhcVQ', 3), ('WLDTE73P', 1)]
- SOL coins 3713, non-SOL coins 44 (12 coins)
- non-SOL sample: vsol 0.0, sol 0.0, vquote_raw 2713966299, quote_amount_raw 133792667, quote Xsc9qvGR1efVDFGLrVsmkzv3qi45LTBjeUKSPmx9qEh
- trades with buyback>0: 2287/3713; buyback_bps values [(5000, 2288), (0, 1425)]
- fee/sol in bps: median 95.00 (fee alone) vs 142.50 (fee + buyback); event fee_bps [(95, 2849), (0, 864)]
- cashback_bps [(0, 3707), (30, 6)], holder_rewards_bps [(0, 3318), (30, 395)], ix [('sell', 1704), ('buy', 1286), ('buy_exact_quote_in', 444), ('buy_exact_sol_in', 279)], mayhem 1425
- zero-SOL trades: 45 (non-SOL share among them: 44)
- migrations 1, post-complete buys 0, completes 1

## pump_amm (PumpSwap), 60 s: 27832 txs, 13697 trades decoded from logs, pool creates 2
- 'Program data' discriminators seen: [('3e2f370aa503dc2a', 7789), ('67f4521f2cf57777', 5908), ('5632504802010000', 330), ('5632504802020000', 330), ('5632504802030000', 330)]
- reserves timing on consecutive trades in the same pool: 13307 pairs, consistent with BEFORE-trade 13306, AFTER-trade 0
- sample: fee bps total 30 (lp 25 / protocol 5 / creator 0), vquote_raw 0
- fee totals seen: [(30, 7631), (105, 2559), (100, 1087), (125, 629), (120, 619), (110, 291)]
