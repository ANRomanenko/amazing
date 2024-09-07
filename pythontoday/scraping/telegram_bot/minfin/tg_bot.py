import json
import datetime
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hcode, hunderline, hbold, hlink
from config import token, user_id
from minfin import check_news_update

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

# @dp.message_handler(commands="start")
# async def get_start(message: types.Message):
#     await message.answer("Wat's up Doc?")
    
@dp.message_handler(commands="all_news")
async def get_all_news(message: types.Message):
    with open("minfin.json", encoding="utf-8") as file:
        news_dict = json.load(file)

    for k, v in sorted(news_dict.items()):
        news = f"{hbold(datetime.datetime.fromtimestamp(v['item_date_timestamp']))}\n" \
        f"{hlink(v['item_title'],v['item_url'])}"

        await message.answer(news)

if __name__ == "__main__":
    executor.start_polling(dp)