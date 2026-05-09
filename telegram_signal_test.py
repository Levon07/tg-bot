import asyncio
from telegram import Bot
from signal_engine import generate_signal

TOKEN = "8775311245:AAGswPvlbmERzaAALjejfqbzHmgbgMqs8RE"
CHAT_ID = 1233256209


async def main():
    bot = Bot(token=TOKEN)

    signal = generate_signal()

    message = f"""
BTC/USDT SIGNAL

ACTION: {signal['action']}
PRICE: {signal['price']}
SCORE: {signal['score']}

STATUS: {'ENTER NOW' if signal['action'] != 'NO TRADE' else 'WAIT'}
"""

    await bot.send_message(chat_id=CHAT_ID, text=message)

    print("sent")


asyncio.run(main())