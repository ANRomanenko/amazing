from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hbold, hunderline, hlink, hcode
import json
import datetime
from config import token, user_id


bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

# @dp.message_handler(commands='start')
# async def get_start(message: types.Message):
#     await message.reply("What's up Doc?")

@dp.message_handler(commands='all_news')
async def get_all_news(message: types.Message):
    with open("minfin2.json", encoding="utf-8") as f:
        news_dict = json.load(f)
    
    for k, v in sorted(news_dict.items()):
        news = f"{hbold(datetime.datetime.fromtimestamp(v['item_date_timestamp']))}\n" \
               f"{hlink(v['item_title'], v['item_url'])}\n"
            #    f"{hunderline(v['item_title'])}\n" \
        
        await message.answer(news)


@dp.message_handler(commands='last_five')
async def get_last_five_news(message: types.Message):
    with open("minfin2.json", encoding="utf-8") as f:
        news_dict = json.load(f)

    for k, v in news_dict.items()[-5:]:
        news = f"{hbold(datetime.datetime.fromtimestamp(v['item_date_timestamp']))}\n" \
               f"{hlink(v['item_title'], v['item_url'])}\n"
            #    f"{hunderline(v['item_title'])}\n" \
        
        await message.answer(news)

if __name__ == "__main__":
    executor.start_polling(dp)