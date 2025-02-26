import os
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from dotenv import load_dotenv

load_dotenv()


TOKEN = os.getenv("TOKEN")


bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    await  message.answer("hello this is your first bot!!!, whats your name?")


@dp.message(Command("info"))
async def help_(message: types.Message):
    await  message.answer("nice")


@dp.message()
async def echo(message: types.Message):
    if message.sticker:
        await message.answer(f"{message.sticker.file_id}")

    if message.text == "sabina":
        await message.reply("hello bot")
    elif message.text == "f" or "w":
        await message.reply("что вы делаете в моем холодосе")
    else:
        await message.answer(f"you write {message.text}")

async def main():
    print("bot startes...")
    await  dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

