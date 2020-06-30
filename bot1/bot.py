# coding=utf-8
import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

# Добавляем обработчик сообщений, который проверяет команды, в нашем случае это команда /start
@bot.message_handler(commands=['start'])
def startpage(message):
    # Создаем клавиатуру, с единственной кнопкой "Начать"
    startmenu = types.ReplyKeyboardMarkup(True, True)
    startmenu.row('Начать')
    # Отправляем сообщение и отправляем подключение клавиатуры
    bot.send_message(message.chat.id, 'Добро пожаловать!✋🏻 \nЯ бесплатный образовательный бот!👨🏻‍🏫\nБлагодаря нашим курсам, вы сможете найти любимую профессию, научится зарабатывать деньги и просто обрести полезные навыки!', reply_markup=startmenu)

#Добавляем обработчик сообщений, который проверяет тип сообщения "Текст"
@bot.message_handler(content_types=['text'])
def main(message):
    # Проверяем какое сообщение нам пришло, на русском языке код выглядит так "Если текст который отправил пользователь РАВЕН СЛОВУ "Начать", то у нас будет выполняться это действие"
    if message.text == 'Начать':
        # Мы присваиваем переменной "send" метод "Отправка сообщения"
        send = bot.send_message(message.chat.id, 'Введите ваше имя:')
        # Здесь мы делаем следующий шаг, который изначально будет отправлять переменную "send", а потом переходит к следующей функции под названием "next1"
        bot.register_next_step_handler(send, next1)
    # Проверяем какое сообщение нам пришло, на русском языке код выглядит так "Если текст который отправил пользователь РАВЕН СЛОВУ "Бизнес", то у нас будет выполняться это действие"
    elif message.text == 'Бизнес':
        if business == 'business':
            # Создаем клавиатуру
            option1 = types.ReplyKeyboardMarkup(True, False)
            option1.row('Курс1')
            option1.row('Курс2')
            option1.row('Курс3')
            option1.row('Курс4')
            option1.row('Назад')
            # Отправляем сообщение и отправляем подключение клавиатуры
            bot.send_message(message.chat.id, 'Выберите курс:', reply_markup=option1)
    # Проверяем какое сообщение нам пришло, на русском языке код выглядит так "Если текст который отправил пользователь РАВЕН СЛОВУ "Программирование", то у нас будет выполняться это действие"
    elif message.text == 'Программирование':
        if business == 'business':
            # Создаем клавиатуру
            option2 = types.ReplyKeyboardMarkup(True, False)
            option2.row('C#')
            option2.row('Python')
            option2.row('C++')
            option2.row('Delphi')
            option2.row('Назад')
            # Отправляем сообщение и отправляем подключение клавиатуры
            bot.send_message(message.chat.id, 'Выберите язык программирования:', reply_markup=option2)
    # Проверяем какое сообщение нам пришло, на русском языке код выглядит так "Если текст который отправил пользователь РАВЕН СЛОВУ "Лайфаки", то у нас будет выполняться это действие"
    elif message.text == 'Лайфаки':
        if business == 'business':
            # Создаем клавиатуру
            option3 = types.ReplyKeyboardMarkup(True, False)
            option3.row('Лайфак1')
            option3.row('Лайфак2')
            option3.row('Лайфак3')
            option3.row('Лайфак4')
            option3.row('Назад')
            # Отправляем сообщение и отправляем подключение клавиатуры
            bot.send_message(message.chat.id, 'Выберите лайфак:', reply_markup=option3)
    # Проверяем какое сообщение нам пришло, на русском языке код выглядит так "Если текст который отправил пользователь РАВЕН СЛОВУ "Фитнес", то у нас будет выполняться это действие"
    elif message.text == 'Фитнес':
        if business == 'business':
            # Создаем клавиатуру
            option4 = types.ReplyKeyboardMarkup(True, False)
            option4.row('Питание')
            option4.row('Упражнения')
            option4.row('Пресс')
            option4.row('Фитнес клубы')
            option4.row('Назад')
            # Отправляем сообщение и отправляем подключение клавиатуры
            bot.send_message(message.chat.id, 'Выберите:', reply_markup=option4)
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
    global business
    business = 'business'
    # Создаем клавиатуру
    option = types.ReplyKeyboardMarkup(True, False)
    option.row('Бизнес')
    option.row('Программирование')
    option.row('Лайфаки')
    option.row('Фитнес')
    # Отправляем сообщение и отправляем подключение клавиатур
    bot.send_message(message.chat.id, 'Хорошо, выберите тематику курсов?', reply_markup=option)


bot.polling()
