import asyncio
from telegram import Bot

TOKEN = "8775311245:AAGswPvlbmERzaAALjejfqbzHmgbgMqs8RE"


async def main():
    bot = Bot(token=TOKEN)

    updates = await bot.get_updates()

    print(updates)


asyncio.run(main())