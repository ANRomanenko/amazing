import asyncio
import datetime
import json
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from config import token, user_id
from autoria import check_news_update

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["Все авто", "Последния 5 авто", "Свежие новости"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("Лента новостей", reply_markup=keyboard)


@dp.message_handler(Text(equals="Все авто"))
async def get_all_auto(message: types.Message):
    with open('news_dict.json', encoding='utf-8') as file:
        news_dict = json.load(file)

    for k, v in sorted(news_dict.items()): # отдаём значения пользователю и пробегаемся по словарю
        # news = f"<b>{datetime.datetime.fromtimestamp(v['article_date_timestamp'])}</b>\n" \
        #        f"<u>{v['article_title']}</u>\n" \
        #        f"<code>{v['article_price']}</code>\n" \
        #        f"{v['article_milage']}\n" \
        #        f"{v['article_city']}\n" \
        #        f"{v['article_fuel']}\n" \
        #        f"{v['article_gearbox']}\n" \
        #        f"{v['article_url']}\n"
        news = f"{hbold(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}\n" \
            f"{hunderline(v['article_title'])}\n" \
            f"{hcode(v['article_price'])}\n" \
            f"{v['article_milage']}\n" \
            f"{v['article_city']}\n" \
            f"{v['article_fuel']}\n" \
            f"{v['article_gearbox']}\n" \
            f"{hlink(v['article_title'], v['article_url'])}"


        await message.answer(news) # отправляем ответ пользователю


@dp.message_handler(Text(equals="Последния 5 авто"))
async def get_five_last_auto(message: types.Message):
    with open('news_dict.json', encoding='utf-8') as file:
        news_dict = json.load(file)

    for k, v in sorted(news_dict.items())[-5:]:
        news = f"{hbold(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}\n" \
            f"{hunderline(v['article_title'])}\n" \
            f"{hcode(v['article_price'])}\n" \
            f"{v['article_milage']}\n" \
            f"{v['article_city']}\n" \
            f"{v['article_fuel']}\n" \
            f"{v['article_gearbox']}\n" \
            f"{hlink(v['article_title'], v['article_url'])}"


        await message.answer(news) # отправляем ответ пользователю


@dp.message_handler(Text(equals="Свежие новости"))
async def get_fresh_auto(message: types.Message):
    fresh_news = check_news_update()

    if len(fresh_news) >= 1:
        for k, v in reversed(fresh_news.items()): 
            news = f"{hbold(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}\n" \
                f"{hunderline(v['article_title'])}\n" \
                f"{hcode(v['article_price'])}\n" \
                f"{v['article_milage']}\n" \
                f"{v['article_city']}\n" \
                f"{v['article_fuel']}\n" \
                f"{v['article_gearbox']}\n" \
                f"{hlink(v['article_title'], v['article_url'])}"
            
            await message.answer(news) # отправляем ответ пользователю
            
    else:
        await message.answer('Пока нет свежих новостей...') # отправляем ответ пользователю


async def news_every_minute():
    while True:
        fresh_news = check_news_update()

        if len(fresh_news) >= 1:
            for k, v in reversed(fresh_news.items()): 
                news = f"{hbold(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}\n" \
                    f"{hunderline(v['article_title'])}\n" \
                    f"{hcode(v['article_price'])}\n" \
                    f"{v['article_milage']}\n" \
                    f"{v['article_city']}\n" \
                    f"{v['article_fuel']}\n" \
                    f"{v['article_gearbox']}\n" \
                    f"{hlink(v['article_title'], v['article_url'])}"
                
                await bot.send_message(user_id, news, disable_notification=False) # отправляем ответ пользователю

        else:
            await bot.send_message(user_id, "Пока нет свежих новостей...", disable_notification=True)

        await asyncio.sleep(180)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(news_every_minute())
    executor.start_polling(dp)