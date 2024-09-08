import asyncio
import json
import datetime
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hcode, hunderline, hbold, hlink
from aiogram.dispatcher.filters import Text
from config import token, user_id
from minfin import check_news_update

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def get_start(message: types.Message):
    start_buttons = ["Все новости", "Последние 5 новостей", "Свежие новости"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer("Лента новостей", reply_markup=keyboard)
    

@dp.message_handler(Text(equals="Все новости"))
async def get_all_news(message: types.Message):
    with open("minfin.json", encoding="utf-8") as file:
        news_dict = json.load(file)

    for k, v in sorted(news_dict.items()):
        news = f"{hbold(datetime.datetime.fromtimestamp(v['item_date_timestamp']))}\n" \
        f"{hlink(v['item_title'],v['item_url'])}"

        await message.answer(news)

@dp.message_handler(Text(equals="Последние 5 новостей"))
async def get_five_last_news(message: types.Message):
    with open("minfin.json", encoding="utf-8") as file:
        news_dict = json.load(file)

    for k, v in sorted(news_dict.items())[-5:]:
        news = f"{hbold(datetime.datetime.fromtimestamp(v['item_date_timestamp']))}\n" \
        f"{hlink(v['item_title'], v['item_url'])}"

        await message.answer(news)


@dp.message_handler(Text(equals="Свежие новости"))
async def get_fresh_news(message: types.Message):
    news_dict = check_news_update()

    if len(news_dict) >= 1:
        for k, v in reversed(news_dict.items()):
            news = f"{hbold(datetime.datetime.fromtimestamp(v['item_date_timestamp']))}\n" \
                   f"{hlink(v['item_title'], v['item_url'])}"

            await message.answer(news)
    
    else:
        await message.answer("Пока нет свежих новстей")

async def news_every_minute():
    while True:
        news_dict = check_news_update()

        if len(news_dict) >= 1:
            for k, v in reversed(news_dict.items()):
                news = f"{hbold(datetime.datetime.fromtimestamp(v['item_date_timestamp']))}\n" \
                    f"{hlink(v['item_title'], v['item_url'])}"

                for user in user_id:
                    await bot.send_message(user, news, disable_notification=True)

        else:
            for user in user_id:
                await bot.send_message(user, "Пока нет свежих новостей....", disable_notification=True)

        await asyncio.sleep(30)



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(news_every_minute())
    executor.start_polling(dp)