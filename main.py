import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handlers.handlers import start_router

bot_loop = asyncio.new_event_loop()
logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()
main_bot = Bot('?token?')


async def shutdown_bot(dp):
    await storage.close()
    await main_bot.close()
    print("Closed!")


if __name__ == "__main__":
    dispatcher = Dispatcher(bot=main_bot, loop=bot_loop, storage=storage)
    dispatcher.include_router(start_router)
    dispatcher.run_polling(main_bot)
