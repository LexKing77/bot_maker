# coding=utf-8
import telebot
import config

from telebot import types

bot = telebot.TeleBot(const.TOKEN)

# Добавляем обработчик сообщений, который проверяет команды, в нашем случае это команда /start
@bot.message_handler(commands=['start'])
def startpg(message):
    # Создаем клавиатуру, с единственной кнопкой "Начать"
    startmenu = types.ReplyKeyboardMarkup(True, True)
    startmenu.row('Начать')
    # Отправляем сообщение и отправляем подключение клавиатуры
    bot.send_message(message.chat.id, 'Добро пожаловать!✋🏻 \nЯ бесплатный образовательный бот!👨🏻‍🏫\nБлагодаря нашим курсам, вы сможете найти любимую профессию, научится зарабатывать деньги и просто обрести полезные навыки!', reply_markup=startmenu)

#Добавляем обработчик сообщений, который проверяет тип сообщения "Текст"
@bot.message_handler(content_types=['text'])
def osnov(message):
    # Проверяем какое сообщение нам пришло, на русском языке код выглядит так "Если текст который отправил пользователь РАВЕН СЛОВУ "Начать", то у нас будет выполняться это действие"
    if message.text == 'Начать':
        # Мы присваиваем переменной "send" метод "Отправка сообщения"
        send = bot.send_message(message.chat.id, 'Введите ваше имя:')
        # Здесь мы делаем следующий шаг, который изначально будет отправлять переменную "send", а потом переходит к следующей функции под названием "next1"
        bot.register_next_step_handler(send, next1)
    # Проверяем какое сообщение нам пришло, на русском языке код выглядит так "Если текст который отправил пользователь РАВЕН СЛОВУ "Бизнес", то у нас будет выполняться это действие"
    elif message.text == 'Бизнес':
        if biznes == 'biznes':
            # Создаем клавиатуру
            vibor1 = types.ReplyKeyboardMarkup(True, False)
            vibor1.row('Курс1')
            vibor1.row('Курс2')
            vibor1.row('Курс3')
            vibor1.row('Курс4')
            vibor1.row('Назад')
            # Отправляем сообщение и отправляем подключение клавиатуры
            bot.send_message(message.chat.id, 'Выберите курс:', reply_markup=vibor1)
    # Проверяем какое сообщение нам пришло, на русском языке код выглядит так "Если текст который отправил пользователь РАВЕН СЛОВУ "Программирование", то у нас будет выполняться это действие"
    elif message.text == 'Программирование':
        if biznes == 'biznes':
            # Создаем клавиатуру
            vibor2 = types.ReplyKeyboardMarkup(True, False)
            vibor2.row('C#')
            vibor2.row('Python')
            vibor2.row('C++')
            vibor2.row('Delphi')
            vibor2.row('Назад')
            # Отправляем сообщение и отправляем подключение клавиатуры
            bot.send_message(message.chat.id, 'Выберите язык программирования:', reply_markup=vibor2)
    # Проверяем какое сообщение нам пришло, на русском языке код выглядит так "Если текст который отправил пользователь РАВЕН СЛОВУ "Лайфаки", то у нас будет выполняться это действие"
    elif message.text == 'Лайфаки':
        if biznes == 'biznes':
            # Создаем клавиатуру
            vibor3 = types.ReplyKeyboardMarkup(True, False)
            vibor3.row('Лайфак1')
            vibor3.row('Лайфак2')
            vibor3.row('Лайфак3')
            vibor3.row('Лайфак4')
            vibor3.row('Назад')
            # Отправляем сообщение и отправляем подключение клавиатуры
            bot.send_message(message.chat.id, 'Выберите лайфак:', reply_markup=vibor3)
    # Проверяем какое сообщение нам пришло, на русском языке код выглядит так "Если текст который отправил пользователь РАВЕН СЛОВУ "Фитнес", то у нас будет выполняться это действие"
    elif message.text == 'Фитнес':
        if biznes == 'biznes':
            # Создаем клавиатуру
            vibor4 = types.ReplyKeyboardMarkup(True, False)
            vibor4.row('Питание')
            vibor4.row('Упражнения')
            vibor4.row('Пресс')
            vibor4.row('Фитнес клубы')
            vibor4.row('Назад')
            # Отправляем сообщение и отправляем подключение клавиатуры
            bot.send_message(message.chat.id, 'Выберите:', reply_markup=vibor4)
    # Проверяем какое сообщение нам пришло, на русском языке код выглядит так "Если текст который отправил пользователь РАВЕН СЛОВУ "Назал", то у нас будет выполняться это действие"
    elif message.text == 'Назад':
        # Так делается, для того, чтобы перейти к фукнции с назаваением "next2"
        next2(message)

# Создаем функцию, для того, чтобы ответить на первое сообщение "Введите ваше имя:"
def next1(message):
    # Мы присваиваем переменной "send" метод "Отправка сообщения"
    send = bot.send_message(message.chat.id, 'Очень приятно {name}, введите ваш возвраст:'.format(name=message.text))
    # Здесь мы делаем следующий шаг, который изначально будет отправлять переменную "send", а потом переходит к следующей функции под названием "next2"
    bot.register_next_step_handler(send, next2)

# Создаем функцию, для того, чтобы ответить на сообщение "Очень приятно {name},Введите ваш возвраст:"
def next2(message):
    global biznes
    biznes = 'biznes'
    # Создаем клавиатуру
    vibor = types.ReplyKeyboardMarkup(True, False)
    vibor.row('Бизнес')
    vibor.row('Программирование')
    vibor.row('Лайфаки')
    vibor.row('Фитнес')
    # Отправляем сообщение и отправляем подключение клавиатуры
    bot.send_message(message.chat.id, 'Хорошо, выберите тематику курсов?', reply_markup=vibor)


bot.polling()
