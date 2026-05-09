import ccxt

exchange = ccxt.binance({"options": {"defaultType": "future"}})

def get_liquidity():
    ohlcv = exchange.fetch_ohlcv("BTC/USDT", timeframe="1h", limit=100)

    highs = [c[2] for c in ohlcv]
    lows = [c[3] for c in ohlcv]
    closes = [c[4] for c in ohlcv]

    last = closes[-1]

    # recent swing zones
    recent_high = max(highs[-20:])
    recent_low = min(lows[-20:])

    # detect liquidity sweeps
    sweep_high = last > recent_high
    sweep_low = last < recent_low

    # equal highs / lows (simple clustering)
    eq_high = abs(highs[-1] - highs[-2]) / highs[-1] < 0.002
    eq_low = abs(lows[-1] - lows[-2]) / lows[-1] < 0.002

    return {
        "sweep_high": sweep_high,
        "sweep_low": sweep_low,
        "eq_high": eq_high,
        "eq_low": eq_low,
        "price": last
    }