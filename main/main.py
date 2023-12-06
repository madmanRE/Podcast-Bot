import asyncio
import logging
import re

import sys

sys.path.append("..")

from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types.input_file import InputFile

from config import TOKEN

from converter import main_converter

bot = Bot(token=TOKEN)
dp = Dispatcher()

text_plug = (
    "Я принимаю ссылки на видеоролики в YouTube и возвращаю подкаст в формате mp3."
)


@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.reply(text=f"Привет, {message.from_user.full_name}!\n{text_plug}\n")


@dp.message(Command("help"))
async def handle_help(message: types.Message):
    text = f"{text_plug}"
    await message.answer(text=text)


@dp.message()
async def echo_message(message: types.Message):
    if re.match(".*youtu\.?be.*", message.text):
        await message.answer(text="Началась обработка файла, ожидайте...")

        audio_path = main_converter.download_audio(
            r"{path}".format(path=message.text.strip())
        )

        if audio_path:
            await message.reply_audio(audio=types.FSInputFile(path=audio_path))

    else:
        text = f"{text_plug}"
        await message.answer(text=text)


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
