import ccxt

exchange = ccxt.binance({"options": {"defaultType": "future"}})


def get_structure():

    ohlcv = exchange.fetch_ohlcv("BTC/USDT", timeframe="1h", limit=100)

    highs = [c[2] for c in ohlcv]
    lows = [c[3] for c in ohlcv]
    closes = [c[4] for c in ohlcv]

    last = closes[-1]

    # =========================
    # SAFETY CHECK (avoid index errors)
    # =========================
    if len(highs) < 60:
        return {
            "trend": "neutral",
            "bos_up": False,
            "bos_down": False,
            "choch_up": False,
            "choch_down": False,
            "price": last,
            "swing_high": max(highs),
            "swing_low": min(lows)
        }

    # =========================
    # SWING STRUCTURE
    # =========================

    prev_high = max(highs[-30:])
    prev_low = min(lows[-30:])

    mid_high = max(highs[-60:-30])
    mid_low = min(lows[-60:-30])

    swing_high = max(highs[-20:])
    swing_low = min(lows[-20:])

    # =========================
    # MARKET STRUCTURE LOGIC
    # =========================

    bos_up = last > prev_high
    bos_down = last < prev_low

    choch_up = (mid_low < prev_low) and (last > mid_high)
    choch_down = (mid_high > prev_high) and (last < mid_low)

    # =========================
    # TREND FILTER
    # =========================

    trend = "bullish" if closes[-1] > closes[-20] else "bearish"

    # =========================
    # OUTPUT
    # =========================

    return {
        "trend": trend,
        "bos_up": bos_up,
        "bos_down": bos_down,
        "choch_up": choch_up,
        "choch_down": choch_down,
        "price": last,
        "swing_high": swing_high,
        "swing_low": swing_low
    }