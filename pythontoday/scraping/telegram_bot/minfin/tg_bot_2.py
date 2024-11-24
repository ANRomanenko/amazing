import json
import datetime
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from config import token, user_id


bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


# @dp.message_handler(commands='start')
# async def start(message: types.Message):
#     await message.reply("Wat's up Doc?")

@dp.message_handler(commands='all_news')
async def get_all_news(message: types.Message):
    with open("minfin2.json", encoding="utf-8") as file:
        news_dict = json.load(file)
    print(news_dict)


if __name__ == "__main__":
    executor.start_polling(dp)