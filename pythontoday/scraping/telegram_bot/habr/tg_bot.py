import asyncio
import json
import datetime
from habr import check_news_update
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
from aiogram.dispatcher.filters import Text
from config import token, user_id

bot = Bot(token=token, parse_mode=types.ParseMode.HTML) # Создаём объект бота в параметры которого передаём token
dp = Dispatcher(bot) # для управления хендлерами создаём объект диспетчер (создаё в качетсве параметра нашего бота (bot))


@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_button = ["Все новости", "Последние 5 новостей", "Свежие новости"] # кнопки для наших новостей
    # Создаём объект клавиатуры
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_button)

    await message.answer("Лента новостей", reply_markup=keyboard)

@dp.message_handler(Text(equals="Все новости"))
async def get_all_news(message: types.Message):
    with open("habr.json", encoding="utf-8") as file:
        news_dict = json.load(file)

    # for k, v in sorted(news_dict.items()):
    #     news = f"<b>{datetime.datetime.fromtimestamp(v['article_date_timestamp'])}</b>\n" \
    #         f"<u>{v['article_title']}</u>\n" \
    #         f"{v['article_url']}"
        
    for k, v in sorted(news_dict.items()):
        news = f"{hbold(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}\n" \
            f"{hlink(v['article_title'],v['article_url'])}"
            # f"{hunderline(v['article_title'])}\n" \
         
        await message.answer(news)

@dp.message_handler(Text(equals="Последние 5 новостей"))
async def get_five_last_news(message: types.Message):
    with open("habr.json", encoding="utf-8") as file:
        news_dict = json.load(file)

    for k, v in sorted(news_dict.items())[-5:]:
        news = f"{hbold(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}\n" \
            f"{hlink(v['article_title'],v['article_url'])}"
            # f"{hunderline(v['article_title'])}\n" \
         
        await message.answer(news)


@dp.message_handler(Text(equals="Свежие новости"))
async def get_fresh_news(message: types.Message):
    fresh_news = check_news_update()

    if len(fresh_news) >= 1:
        for k, v in reversed(fresh_news.items()):
            news = f"{hbold(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}\n" \
                f"{hlink(v['article_title'],v['article_url'])}"
                # f"{hunderline(v['article_title'])}\n" \

            await message.answer(news)

    else:
        await message.answer("Пока нет свежих новостей")


async def news_every_minute():
    while True:
        fresh_news = check_news_update()

        if len(fresh_news) >= 1:
            for k, v in reversed(fresh_news.items()):
                news = f"{hbold(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}\n" \
                    f"{hlink(v['article_title'],v['article_url'])}"
                    # f"{hunderline(v['article_title'])}\n" \
                
                await bot.send_message(user_id, news, disable_notification=True)
        else:
            await bot.send_message(user_id, "Пока нет свежих новостей...", disable_notification=True)

        await asyncio.sleep(20)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()# Создаём петлю
    loop.create_task(news_every_minute())# создаём новую задачу
    executor.start_polling(dp)
