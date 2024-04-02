import asyncio
from config import TOKEN
from app.handlers import router

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode

from app.database.models import create_database
import app.database.requests as db


async def main():
    await create_database()

    dp = Dispatcher()
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    dp.include_routers(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())