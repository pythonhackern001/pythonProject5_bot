from aiogram import Bot, Dispatcher, types, executor
import logging

TOKEN = "5693031108:AAFRvQ8Vj38Z3CzNeR27zaFOy1XOGX9sbLs"

bot = Bot(token=TOKEN)
logging.basicConfig(level=logging.INFO)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def salomlash(messages: types.Message):
    await messages.reply("salom")



@dp.message_handler()
async def function(messages: types.Message):
    data = messages.text.split()
    if data[0] == "shifrlash":
        place = ""
        for i in data[1]:
            place += chr(ord(i) + 2)
        await messages.answer(place)
    elif data[0] == "deshifrlash":
        place = ""
        for i in data[1]:
            place += chr(ord(i) - 2)
        await messages.answer(place)
    else:
        await messages.answer("Entered Wrong 🤷‍♂️🤦‍♂️😔😔😔🧟‍♂️")


executor.start_polling(dispatcher=dp, skip_updates=False)
