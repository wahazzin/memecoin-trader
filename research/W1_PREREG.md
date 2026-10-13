# Pre-registration W1 — Do "good" memecoin wallets stay good, and can we copy them after costs?

**Written 2026-10-13, before any wallet-level analysis of the recorded data.** Up to now the recorded
trades were only used for coin-level checks (M1 checks, bot smoke tests); no wallet has been ranked, scored
or looked up. Git timestamp = proof. Changes only at the bottom, dated, before the test runs.

## 1. Question and prior

Owner (2026-10-13): watch hundreds of memecoin traders' wallets, learn what they buy, when they buy and
sell, and see if copying them is worth it. Two questions, tested in this order:

- **W1a (skill):** do wallets that made the most money in one period also make money in the NEXT period,
  more than other active wallets? If not, the "top traders" were lucky, and there is nothing to copy.
- **W1b (copyable):** if we buy a few seconds AFTER a top wallet buys, and sell a few seconds after it sells,
  at real prices with all our costs, is expectancy per trade > 0 and better than copying random wallets?

Prior: low for W1b. With tens of thousands of wallets, some look brilliant by pure luck. Many top wallets
are insiders (devs, bundlers, snipers) whose edge is being first, which we can't copy. Every copy buy pays
a worse price than the wallet did, and some well-known wallets bait copy-traders and sell into them.
W1a might pass and W1b still fail: "skilled" and "copyable" are different questions.

## 2. Data

Our own recording (`trades.parquet`): every pump.fun and PumpSwap trade of SOL-quoted coins during their
first 100 minutes, with wallet, SOL amount, tokens, fees and reserves. Data from 2026-10-07 ~20:45 UTC;
the test runs once there are at least 14 full days. Coins whose first 100 minutes overlap a recorder gap
are excluded. Non-SOL coins are excluded (A2 of M1/M2).

**Blind spot (stated now):** trades after a coin's first 100 minutes are not recorded. A wallet that still
holds a coin at the 100-minute mark has an unknown result on it.

## 3. Wallet results (fixed)

For each wallet × coin, inside the 100-minute window:
- **Closed position:** the wallet sold at least 90% of the tokens it bought. P&L = SOL received from sells
  − SOL paid for buys − every pump.fun/PumpSwap fee shown in its trade events. Priority fees are not in
  the events and are ignored for THEIR P&L (this flatters them slightly; our copy P&L in §5 pays them).
- **Open position:** anything else. Counted, never scored.

**Eligible wallets:** ≥ 20 closed positions in the design period, AND open positions ≤ 30% of all its
positions (otherwise we can't see its results), AND it is not the creator of the coin (creator positions
are dropped).

Not excluded: snipers and bundlers. We don't remove them by guessing; W1b's delay deals with them,
because a copy buy 2 s later doesn't get their price.

## 4. W1a — persistence (skill vs luck)

- **Split:** chronological, DESIGN = first 60% of full days, HOLDOUT = last 40%. Holdout looked at once.
- **Top group:** the 50 eligible wallets with the highest total P&L in DESIGN.
- **Holdout measure:** each wallet's mean P&L per closed position in HOLDOUT. Only wallets with ≥ 5
  holdout closed positions count.
- **PASS W1a only if both:**
  1. the top group's mean holdout P&L per position > 0, with a 95% bootstrap CI (resampling wallets,
     10,000×) whose lower bound > 0; and
  2. the top group beats the other eligible wallets: bootstrap of the difference in means, lower bound
     > 0.
- Also reported (cannot pass): Spearman rank correlation of design vs holdout P&L across all eligible
  wallets.

## 5. W1b — copy test (only meaningful if W1a passes, but always run and reported)

For every HOLDOUT position opened by a top-group wallet (its first buy in a coin):
- **Our buy:** 0.5 SOL at the first recorded trade ≥ 2 s after their buy (same delay as the paper bot), priced
  with the verified curve formula from that trade's reserves, so later buyers' price impact is included.
  If the coin is graduated, PumpSwap pool reserves and fee from the event are used (A2).
- **Our sell:** when the wallet has sold ≥ 50% of its tokens, at the first trade ≥ 2 s after that sell.
  Backstops: 60 minutes held, or the 100-minute window ending (sold at the last recorded trade's reserves).
- **Costs (COST_FACTORS.md):** the coin's actual fee from events per side, priority fee 0.0015 SOL per side,
  network fee, account rent 0.00204 SOL refunded on close.
- **Control:** the same rules, copying the same number of positions from wallets drawn at random from
  the eligible wallets outside the top 50, matched by hour of the day.
- **PASS W1b only if all three:**
  1. copy expectancy per trade > 0, with t ≥ 2 (trades grouped by hour);
  2. copy expectancy − control expectancy > 0, with t ≥ 2 (hour-matched); and
  3. ≥ 300 copied trades in the holdout.
- Secondary (reported only): delays of 1 s and 5 s; and copying the top 10 instead of the top 50.

## 6. Verdict

- W1a PASS + W1b PASS → copy-trading becomes a candidate paper-bot arm, run as its own forward test
  specified separately, against the random-copy control.
- W1a PASS + W1b fail → skill exists but can't be copied with our speed and costs. The wallets' TIMING may
  still be studied as a feature in a later pre-registered test.
- W1a fail → "top traders" were luck at this sample size. Nothing to copy.
- Anything else → NO EVIDENCE (most likely, stated now).

## 7. Validation before real data

As with M1/M2, the code runs first on synthetic data:
- planted skilled wallets that keep winning and can be copied → must PASS;
- all wallets random → must return NO EVIDENCE.

## 8. Ways we could fool ourselves

| Risk | Control |
|---|---|
| Lucky wallets look skilled | Picked in design, judged only in a later, untouched holdout |
| Insiders/devs look like geniuses | Creator positions dropped; copy test buys 2 s late at real reserves |
| Survivorship (only seeing winners) | Every wallet and every coin recorded from birth, losers included |
| Hidden losses on long holds | Open positions counted, not scored; wallets mostly open are excluded |
| Tuning the top-N or delay | Top 50 and 2 s fixed here; other values reported only |
| One trader with many wallets | Unknowable from this data; stated as a limit |
| Bait wallets that sell to copiers | That is exactly what W1b measures, at real later prices |
