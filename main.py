
import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from model import predict

API_TOKEN = 'API_TOKEN_HERE'


logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage = storage)


@dp.message_handler(commands = ['start'])
async def start_command(message: types.Message):
    await message.answer('Введите запрос')


@dp.message_handler(content_types=['text'])
async def start_command(message: types.Message):
    await message.answer('Обрабатываю...')
    await message.answer(predict(message.text))
    


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

