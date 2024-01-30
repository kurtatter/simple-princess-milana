import asyncio
import string
from datetime import timedelta

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler

import config
from parser.service import TheatreParser
from keyboards import main_kb
from templates import get_event_template

bot = Bot(config.BOT_TOKEN, parse_mode='html')
dp = Dispatcher()
parser = TheatreParser()
scheduler = AsyncIOScheduler(timezone="Europe/Moscow")


@dp.message(CommandStart())
async def start(message: Message):
    scheduler.add_job(send_message_interval, 'interval', seconds=int(config.UPDATE_TIME_INTERVAL),
                      kwargs={'message': message})
    await message.answer("Aloha!", reply_markup=main_kb)


@dp.message(F.text.lower() == "афиша [с картинками]")
async def events(message: Message):
    string.Template(message.text).safe_substitute()
    theatre_events = parser.get_events_json()['events']
    for event in theatre_events:
        img_url = event['posterImage']['url']

        await bot.send_photo(message.chat.id, photo=img_url, caption=get_event_template(event))


@dp.message(F.text.lower() == "афиша [список]")
async def events(message: Message):
    string.Template(message.text).safe_substitute()
    theatre_events = parser.get_events_json()['events']
    response_text = f'{message.chat.id}\nАфиша:\n'
    for event in theatre_events:
        response_text += get_event_template(event)
        response_text += '-' * 24
    await message.answer(response_text)


async def send_message_interval(message: Message):
    await message.answer("ALarm!")


async def main():
    scheduler.start()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
