import logging
from transliterate import to_latin,to_cyrillic
from  aiogram import Bot,Dispatcher,executor,types
API_TOKEN="7230850013:AAEA0FfC90aPo36UtrPVLjey6R2e88k5Fl8"
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.reply("Salom!\nBu lotindan kirilga yoki krilldan lotinchaga o'tkazuvchi bot!\nMatnni kiriting.")



@dp.message_handler()
async def change(message: types.Message):
    msg=message.text
    javob=lambda msg:to_cyrillic(msg) if msg.isascii() else to_latin(msg)

    await message.answer(javob(msg))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)