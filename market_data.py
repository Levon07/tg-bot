import ccxt

exchange = ccxt.binance({
    "options": {"defaultType": "future"}
})

def get_btc_data():
    ohlcv = exchange.fetch_ohlcv("BTC/USDT", timeframe="1h", limit=100)

    closes = [c[4] for c in ohlcv]

    return {
        "last_price": closes[-1],
        "trend": "up" if closes[-1] > closes[-20] else "down"
    }


if __name__ == "__main__":
    print(get_btc_data())