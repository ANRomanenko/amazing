import asyncio
import json
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hbold, hunderline, hlink, hcode
from aiogram.dispatcher.filters import Text
from config import token, user_id
from prom import check_news_update

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["Все товары", "Последние 5 товаров", "Свежие товары"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer("Лента новостей", reply_markup=keyboard)


@dp.message_handler(Text(equals="Все товары"))
async def get_all_news(message: types.Message):
    with open("prom.json", encoding="utf-8") as file:
        news_dict = json.load(file)
    
    for k, v in sorted(news_dict.items()):
        news = f"{hbold(v['product_title'])}\n" \
        f"{hcode(v['product_price'])}\n" \
        f"{hunderline(v['product_delivery'])}\n" \
        f"{v['product_company']}\n" \
        f"{hlink(v['product_title'], v['product_url'])}"

        await message.answer(news)

@dp.message_handler(Text(equals="Последние 5 товаров"))
async def get_five_last_news(message: types.Message):
    with open("prom.json", encoding="utf-8") as file:
        news_dict = json.load(file)
    
    for k, v in sorted(news_dict.items())[-5:]:
        news = f"{hbold(v['product_title'])}\n" \
        f"{hcode(v['product_price'])}\n" \
        f"{hunderline(v['product_delivery'])}\n" \
        f"{v['product_company']}\n" \
        f"{hlink(v['product_title'], v['product_url'])}"

        await message.answer(news)

@dp.message_handler(Text(equals="Свежие товары"))
async def get_fresh_news(message: types.Message):
    news_dict = check_news_update()

    if len(news_dict) >= 1:

        for k, v in reversed(news_dict.items()):
            news = f"{hbold(v['product_title'])}\n" \
            f"{hcode(v['product_price'])}\n" \
            f"{hunderline(v['product_delivery'])}\n" \
            f"{v['product_company']}\n" \
            f"{hlink(v['product_title'], v['product_url'])}"

            await message.answer(news)

    else:
        await message.answer("Пока нет свежих товаров...")


async def news_every_minute():
    while True:
        fresh_news = check_news_update()

        if len(fresh_news) >= 1:

            for k, v in reversed(fresh_news.items()):
                news = f"{hbold(v['product_title'])}\n" \
                f"{hcode(v['product_price'])}\n" \
                f"{hunderline(v['product_delivery'])}\n" \
                f"{v['product_company']}\n" \
                f"{hlink(v['product_title'], v['product_url'])}"

                for user in user_id:
                    await bot.send_message(user, news, disable_notification=False)
        else:
            for user in user_id:
                await bot.send_message(user, "Пока нет свежих товаров...", disable_notification=True)

        await asyncio.sleep(180)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(news_every_minute())
    executor.start_polling(dp)

