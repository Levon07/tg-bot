import asyncio
import os
from telegram import Bot
from signal_engine import generate_signal

CHAT_ID = int(os.getenv("TELEGRAM_CHAT_ID"))


async def main():

    token = os.getenv("TELEGRAM_BOT_TOKEN")
    bot = Bot(token=token)

    signal = generate_signal()

    message = f"""
BTC/USDT SIGNAL

ACTION: {signal['action']}
PRICE: {signal['price']}
SCORE: {signal['score']}
HTF: {signal['htf_bias']}
VOL: {signal['volatility']}

ENTRY: {signal['entry']}
SL: {signal['stop_loss']}
TP1: {signal['take_profit_1']}
TP2: {signal['take_profit_2']}

STATUS: {'ENTER NOW' if signal['action'] != 'NO TRADE' else 'WAIT'}
"""

    await bot.send_message(chat_id=CHAT_ID, text=message)

    print("sent")


if __name__ == "__main__":
    asyncio.run(main())