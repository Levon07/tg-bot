import ccxt

exchange = ccxt.binance({"options": {"defaultType": "future"}})


def get_htf_bias():
    # Higher timeframe (4H) context filter
    ohlcv = exchange.fetch_ohlcv("BTC/USDT", timeframe="4h", limit=100)

    closes = [c[4] for c in ohlcv]

    if len(closes) < 20:
        return "neutral"

    last = closes[-1]

    # simple HTF trend filter
    if last > max(closes[-20:]):
        return "bullish"
    elif last < min(closes[-20:]):
        return "bearish"
    else:
        return "neutral"