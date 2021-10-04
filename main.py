from vkbottle import Keyboard, Text
from vkbottle.bot import Bot, Message

bot = Bot(token="042069c40f987a3c04a68c1524d19484d56d9089f8ca2dfd84bbd93e05d50cb3d9df4915f2bcc1c4fd341")
bot.labeler.vbml_ignore_case = True


# git add *
# git commit -m "Somethind edited"
# git push -u origin main
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


@bot.on.message(text="Треугольник <a> <b> <c>")
async def hi_handler(message: Message, a: float, b: float, c: float):
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    await message.answer(f"Площадь равна {s!r}")


@bot.on.message(text="Помощь")
async def hi_handler(message: Message):
    KEYBOARD = Keyboard(one_time=True)
    BUTTON = Text("Записать")
    BUTTON1 = Text("Помощь")
    BUTTON2 = Text("Правила")
    KEYBOARD.add(BUTTON)
    KEYBOARD.add(BUTTON1)
    KEYBOARD.add(BUTTON2)
    KEYBOARD = KEYBOARD.get_json()
    await message.answer(f"Привет. Вот тебе полное объяснение команд:")
    await message.answer("1)'Записать' используется для того, чтобы записать дз на завтра," + "которое ты знаешь.")
    await message.answer("К примеру ты хочешь записать 'Физика п.58 читать и Дидактика стр 15 #3'")
    await message.answer("Пишешь это как 'Записать Физика п.58 читать и Дидактика стр 15 #3'", keyboard=KEYBOARD)


@bot.on.message(text="Правила")
async def hi_handler(message: Message):
    KEYBOARD1 = Keyboard(one_time=True)
    BUTTON = Text("Дз на завтра")
    BUTTON1 = Text("Помощь")
    BUTTON2 = Text("Правила")
    KEYBOARD1.add(BUTTON)
    KEYBOARD1.add(BUTTON1)
    KEYBOARD1.add(BUTTON2)
    KEYBOARD = KEYBOARD1.get_json()
    await message.answer("Правила просты:")
    await message.answer("1. Запрещено спамить командами")
    await message.answer("2. Запрещено писать Всякую фигню в дз")
    await message.answer("3. Если вы имеете хоть какое-то ВЕРНОЕ дз, тогда нажмите помощь и добавьте его",
                         keyboard=KEYBOARD)


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

@bot.on.message(text="Опрос")
async def hi_handler(message: Message):
    await message.answer(f"Привет. Если хочешь пройти опрос, напиши 'Опрос Да',если не хочешь 'Опрос Нет'")


@bot.on.message(text="Опрос Да")
async def hi_handler(message: Message):
    await message.answer(f"Привет,'")


@bot.on.message(text="Рандом фото Алёны ")
async def hi_handler(message: Message,):
    await message.answer(f"f")


bot.run_forever()
