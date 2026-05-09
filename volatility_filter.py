import ccxt
import numpy as np

exchange = ccxt.binance({"options": {"defaultType": "future"}})


def get_atr_filter():

    ohlcv = exchange.fetch_ohlcv("BTC/USDT", timeframe="1h", limit=50)

    highs = np.array([c[2] for c in ohlcv])
    lows = np.array([c[3] for c in ohlcv])
    closes = np.array([c[4] for c in ohlcv])

    tr = np.maximum(
        highs[1:] - lows[1:],
        np.maximum(
            abs(highs[1:] - closes[:-1]),
            abs(lows[1:] - closes[:-1])
        )
    )

    atr = np.mean(tr)

    price = closes[-1]

    volatility = atr / price

    if volatility < 0.003:
        return "low"
    elif volatility > 0.01:
        return "high"
    else:
        return "normal"