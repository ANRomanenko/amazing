import asyncio
import json
import datetime
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hbold, hlink, hunderline, hcode
from aiogram.dispatcher.filters import Text
from minfin2 import check_news_update
from config import token, user_id

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    start_buttons = ["Все новости", "Последние 5 новостей", "Свежие новости"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("Лента новостей", reply_markup=keyboard)
    # await message.reply("Wat's up Doc?")

@dp.message_handler(Text(equals='Все новости'))
async def get_all_news(message: types.Message):
    with open("minfin2.json", encoding="utf-8") as f:
        news_dict = json.load(f)

    for k, v in sorted(news_dict.items()):
        news = f"{hbold(datetime.datetime.fromtimestamp(v['item_date_timestamp']))}\n" \
               f"{hlink(v['item_title'], v['item_url'])}"
        await message.answer(news)

@dp.message_handler(Text(equals='Последние 5 новостей'))
async def get_last_five_news(message: types.Message):
    with open("minfin2.json", encoding="utf-8") as f:
        news_dict = json.load(f)

    for k, v in sorted(news_dict.items())[-5:]:
        news = f"{hbold(datetime.datetime.fromtimestamp(v['item_date_timestamp']))}\n" \
                f"{hlink(v['item_title'], v['item_url'])}"
        await message.answer(news)

@dp.message_handler(Text(equals='Свежие новости'))
async def get_fresh_news(message: types.Message):
    news_dict = check_news_update()

    if len(news_dict) >= 1:
        for k, v in reversed(news_dict.items()):
            news = f"{hbold(datetime.datetime.fromtimestamp(v['item_date_timestamp']))}\n" \
                   f"{hlink(v['item_title'], v['item_url'])}"
            await message.answer(news)

    else:
        await message.answer("Пока нет свежих новостей")

async def news_every_minute():
    while True:
        news_dict = check_news_update()

        if len(news_dict) >= 1:
            for k, v in reversed(news_dict.items()):
                news = f"{hbold(datetime.datetime.fromtimestamp(v['item_date_timestamp']))}\n" \
                       f"{hlink(v['item_title'], v['item_url'])}"
                await bot.send_message(user_id, news, disable_notification=True)

        else:
            await bot.send_message(user_id, "Пока нет светжих новостей...", disable_notification=True)

        await asyncio.sleep(20)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(news_every_minute())
    executor.start_polling(dp)