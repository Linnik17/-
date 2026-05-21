import asyncio
import os
from aiogram import Bot, Dispatcher, types

from ui.keyboard import menu
from modules.username import username_scan
from modules.phone import phone_scan
from modules.email import email_scan
from modules.domain import domain_scan

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

state = {}

@dp.message()
async def handler(message: types.Message):
    text = message.text.strip()
    uid = message.from_user.id

    if text == "/start":
        await message.answer("osint system ready", reply_markup=menu())
        return

    if text == "username scan":
        state[uid] = "username"
        await message.answer("send username")
        return

    if text == "phone scan":
        state[uid] = "phone"
        await message.answer("send phone")
        return

    if text == "email scan":
        state[uid] = "email"
        await message.answer("send email")
        return

    if text == "domain scan":
        state[uid] = "domain"
        await message.answer("send domain")
        return

    mode = state.get(uid)

    if mode == "username":
        await message.answer(await username_scan(text))
        return

    if mode == "phone":
        await message.answer(phone_scan(text))
        return

    if mode == "email":
        await message.answer(email_scan(text))
        return

    if mode == "domain":
        await message.answer(domain_scan(text))
        return

    await message.answer("use /start")

async def main():
    print("bot running")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
