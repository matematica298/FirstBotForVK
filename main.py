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
    BUTTON1 = Text("Помощь")

    # Добавляем клавишу в клавиатуру
    KEYBOARD.add(BUTTON)
    KEYBOARD.add(BUTTON1)

    # Перенос на новую строчку
    # KEYBOARD.row()

    await message.answer("Привет", keyboard=KEYBOARD.get_json())


dz = ''


@bot.on.message(text="Записать <text>")
async def hi_handler(message: Message, text: str):
    global dz
    dz = dz + "\n" + text
    await message.answer(f"Вы записали {text!r}")

@bot.on.message(text="Помощь")
async def hi_handler(message: Message, text: str):
    # Создаем клавиатуру
    KEYBOARD = Keyboard(one_time=True)

    # Создаем клавишу
    BUTTON = Text("Записать")
    BUTTON1 = Text("Помощь")

    # Добавляем клавишу в клавиатуру
    KEYBOARD.add(BUTTON)
    KEYBOARD.add(BUTTON1)

    await message.answer(f"Привет. Вот тебе полное объяснение команд:")
    await message.answer("'Записать' используется для того, чтобы записать дз на завтра,"+"которое ты знаешь.")
    await message.answer("К примеру ты хочешь записать 'Физика п.58 читать и Дидактика стр 15 #3'")
    await message.answer("Пишешь это как 'Записать Физика п.58 читать и Дидактика стр 15 #3'",  keyboard=KEYBOARD.get_json())

@bot.on.message(text="Дз на завтра")
async def hi_handler(message: Message):
    global dz
    await message.answer(dz)

@bot.on.message(text="Очистить дз")
async def hi_handler(message: Message):
    global dz
    dz = ''
    await message.answer(f"Вы Очистили дз")


bot.run_forever()
