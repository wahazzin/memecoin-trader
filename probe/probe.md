# Data probe 2026-10-07 18:19 UTC

## 1. PumpPortal websocket (4.1 min)
- new tokens: 127 (~44,940/day)
- trades on the first 40 new tokens: 0; per token: []
- migrations: 5; other messages: 41
- create fields: ['bondingCurveKey', 'initialBuy', 'is_mayhem_mode', 'marketCapSol', 'mint', 'name', 'pool', 'signature', 'solAmount', 'symbol', 'traderPublicKey', 'txType', 'uri', 'vSolInBondingCurve', 'vTokensInBondingCurve']

## 2. Solana public RPC (wallet history = funding-source checks)
- skipped: no trades captured

## 3. DexScreener / GeckoTerminal
- GeckoTerminal PumpSwap pools: HTTP 200, 20 pools
- GeckoTerminal 1-min OHLCV for one migrated pool: HTTP 200, 1000 candles
- DexScreener token (brand-new pump coin): HTTP 200, [{'chainId': 'solana', 'dexId': 'pumpfun', 'url': 'https://dexscreener.com/solana/f1nlwimesn8u6oqk1wbjrpei7y93xgy42wxfyzdc5pum', 'pairAddress': 'F1nLw
- DexScreener latest paid profiles: HTTP 200, 30

## 4. pump.fun public frontend API
- https://frontend-api-v3.pump.fun/coins/<mint>: HTTP 404, keys ['error', 'message', 'path', 'statusCode', 'timestamp']
