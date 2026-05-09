from telegram import Bot
from signal_engine import generate_signal

TOKEN = "YOUR_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

bot = Bot(token=TOKEN)


def format_message(signal):

    return f"""
BTC/USDT SIGNAL

ACTION: {signal['action']}
PRICE: {signal['price']}
SCORE: {signal['score']}

ENTRY: market / zone (from engine)
STOP LOSS: calculated below structure
TAKE PROFIT 1: liquidity zone
TAKE PROFIT 2: next liquidity

RISK: 1-2% max per trade

STATUS: {'ENTER NOW' if signal['action'] != 'NO TRADE' else 'WAIT'}
"""


def send_signal():
    signal = generate_signal()
    msg = format_message(signal)

    bot.send_message(chat_id=CHAT_ID, text=msg)
    print("sent:", signal)


if __name__ == "__main__":
    send_signal()