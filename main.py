from vkbottle import Keyboard, Text
from vkbottle.bot import Bot, Message

bot = Bot(token="042069c40f987a3c04a68c1524d19484d56d9089f8ca2dfd84bbd93e05d50cb3d9df4915f2bcc1c4fd341")
bot.labeler.vbml_ignore_case = True


@bot.on.message(text="привет")
async def hi_handler(message: Message):
    # Создаем клавиатуру
     KEYBOARD = Keyboard(one_time=True)

    # Создаем клавишу
     BUTTON = Text("Записать")
     BUTTON1 = Text("Помощь")
     BUTTON2 = Text("Правила")

    # Добавляем клавишу в клавиатуру
     KEYBOARD.add(BUTTON)
     KEYBOARD.add(BUTTON1)
     KEYBOARD.add(BUTTON2)

    # Перенос на новую строчку
     KEYBOARD.row()
    # Получаем JSON-развертку клавиатуры
     KEYBOARD = KEYBOARD.get_json()

     await message.answer("Привет", keyboard=KEYBOARD)

dz = ''


@bot.on.message(text="Записать <text>")
async def hi_handler(message: Message, text: str):
    global dz
    users_info = await bot.api.users.get(message.from_id)
    dz = dz + "\n" + text + (" Это оставил: {}".format(users_info[0].first_name)) + (
        "{}".format(users_info[0].last_name))
    await message.answer(f"Вы записали {text!r}")


@bot.on.chat_message(text="Помощь")
async def hi_handler(message: Message,):
    # Создаем клавиатуру
    KEYBOARD = Keyboard(one_time=True)

    # Создаем клавишу
    BUTTON = Text("Записать")
    BUTTON1 = Text("Помощь")
    BUTTON2 = Text("Правила")

    # Добавляем клавишу в клавиатуру
    KEYBOARD.add(BUTTON)
    KEYBOARD.add(BUTTON1)
    KEYBOARD.add(BUTTON2)

    await message.answer(f"Привет. Вот тебе полное объяснение команд:")
    await message.answer("1)'Записать' используется для того, чтобы записать дз на завтра," + "которое ты знаешь.")
    await message.answer("К примеру ты хочешь записать 'Физика п.58 читать и Дидактика стр 15 #3'")
    await message.answer("Пишешь это как 'Записать Физика п.58 читать и Дидактика стр 15 #3'")
    await message.answer("Вот тебе клавиатура...", keyboard=KEYBOARD.get_json())


@bot.on.message(text="Правила")
async def hi_handler(message: Message):
    # Создаем клавиатуру
    # KEYBOARD1 = Keyboard(one_time=True)

    # Создаем клавишу
    # BUTTON = Text("Дз на завтра")
    # BUTTON1 = Text("Помощь")
    # BUTTON2 = Text("Правила")

    # Добавляем клавишу в клавиатуру
    # KEYBOARD1.add(BUTTON)
    # KEYBOARD1.add(BUTTON1)
    # KEYBOARD1.add(BUTTON2)

    await message.answer(f"Правила просты:")
    await message.answer("1. Запрещено спамить командами")
    await message.answer("2. Запрещено писать Всякую фигню в дз")
    await message.answer("3. Если вы имеете хоть какое-то ВЕРНОЕ дз, тогда нажмите помощь и добавьте его")


# await message.answer("Вот тебе клавиатура...", keyboard=KEYBOARD1.get_json())

@bot.on.message(text="Дз на завтра")
async def hi_handler(message: Message):
    global dz
    await message.answer(dz)


@bot.on.message(text="Очистить дз")
async def hi_handler(message: Message):
    global dz
    dz = ''
    await message.answer(f"Вы Очистили дз")


@bot.on.message(text=["Ты бот", 'ботяра'])
async def hi_handler(message: Message):
    await message.answer('Ты бот')


# @bot.on.private_message(text="Соси")
# async def hi_handler(message: Message):
# users_info = await bot.api.users.get(message.from_id)
# await message.answer("Соси {}".format(users_info[0].first_name))


 #'Максим Дудин (yaderniixyecoc2005)'
 #'Адрес:Альпийский переулок, 16'
 #'Координаты : 59.853591, 30.375867'
 #'16 лет , М'

@bot.on.message(text="Опрос")
async def hi_handler(message: Message):
    await message.answer(f"Привет. Если хочешь пройти опрос, напиши 'Опрос Да',если не хочешь 'Опрос Нет'")

@bot.on.message(text="Опрос Да")
async def hi_handler(message: Message):
    await message.answer(f"Привет,'")


@bot.on.message(text="Рандом фото Алёны")
async def hi_handler(message: Message):
    await message.answer(f"")
bot.run_forever()
