from aiogram import Bot, Dispatcher, executor, types
import json
import datetime
from config import token, user_id


bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def get_start(message: types.Message):