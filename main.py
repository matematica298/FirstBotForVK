from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, Text

bot = Bot(token="042069c40f987a3c04a68c1524d19484d56d9089f8ca2dfd84bbd93e05d50cb3d9df4915f2bcc1c4fd341")
bot.labeler.vbml_ignore_case = True


@bot.on.message(text=["привет", 'ку'])
async def hi_handler(message: Message):
    # Создаем клавиатуру
    KEYBOARD = Keyboard(one_time=True)

    # Создаем клавишу
    BUTTON = Text("Записать")
    BUTTON1 = Text("Съесть еще")

    # Добавляем клавишу в клавиатуру
    KEYBOARD.add(BUTTON)
    KEYBOARD.add(BUTTON1)

    # Перенос на новую строчку
    # KEYBOARD.row()

    await message.answer("Привет", keyboard=KEYBOARD.get_json())


@bot.on.message(text="Записать <text>")
async def hi_handler(message: Message, text: str):
    await message.answer(f"Вы записали {text!r}")


@bot.on.message(text="Дз на завтра")
async def hi_handler(message: Message, text: str):
    await message.answer(f" {text!r}")


bot.run_forever()
