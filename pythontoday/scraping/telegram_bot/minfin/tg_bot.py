import json
import datetime
from aiogram import Bot, Dispatcher, executor, types
from config import token, user_id
from minfin import check_news_update

bot = Bot(token=token)
dp = Dispatcher(bot)

# @dp.message_handler(commands="start")
# async def get_start(message: types.Message):
#     await message.answer("Wat's up Doc?")
    
@dp.message_handler(commands="all_news")
async def get_all_news(message: types.Message):
    with open("minfin.json", encoding="utf-8") as file:
        news_dict = json.load(file)

    print(news_dict)

if __name__ == "__main__":
    executor.start_polling(dp)