import asyncio
import json
import datetime
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hbold, hlink, hunderline, hcode
from aiogram.dispatcher.filters import Text
from habr2 import check_news_update
from config import token, user_id

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["Все новости", "Последние 5 новостей", "Свежие новости"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)# Создаём объект клавиатуры
    keyboard.add(*start_buttons)

    await message.answer("Лента новостей", reply_markup=keyboard)

@dp.message_handler(Text(equals="Все новости"))
async def get_all_news(message: types.Message):
    with open("habr_2.json", encoding="utf-8") as file:
        news_dict = json.load(file)

    for k, v in sorted(news_dict.items()):
        news = f"{hbold(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}\n" \
               f"{hlink(v['article_title'], v['article_url'])}"
            #    f"{v['article_title']}\n" \

        await message.answer(news)

@dp.message_handler(Text(equals="Последние 5 новостей"))
async def get_five_last_news(message: types.Message):
    with open("habr_2.json", encoding="utf-8") as file:
        news_dict = json.load(file)

    for k, v in sorted(news_dict.items())[-5:]:
        news = f"{hbold(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}\n" \
               f"{hlink(v['article_title'], v['article_url'])}"
            #    f"{v['article_title']}\n" \

        await message.answer(news)

@dp.message_handler(Text(equals="Свежие новости"))
async def get_fresh_news(message: types.Message):
    fresh_news = check_news_update()

    if len(fresh_news) >= 1:
        for k, v in reversed(fresh_news.items()):
            news = f"{hbold(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}\n" \
                f"{hlink(v['article_title'], v['article_url'])}"
                #    f"{v['article_title']}\n" \

            await message.answer(news)
    else:
        await message.answer("Пока нет свежих новостей...")


async def news_every_minute():
    while True:
        fresh_news = check_news_update()

        if len(fresh_news) >= 1:
            for k, v in reversed(fresh_news.items()):
                news = f"{hbold(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}\n" \
                    f"{hlink(v['article_title'], v['article_url'])}"
                    #    f"{v['article_title']}\n" \
                
                for chat_id in user_id:
                    await bot.send_message(chat_id, news, disable_notification=True)
        else:
            for chat_id in user_id:
                await bot.send_message(chat_id, "Пока нет свежих новостей...", disable_notification=True)
        
        await asyncio.sleep(20)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(news_every_minute())
    executor.start_polling(dp)