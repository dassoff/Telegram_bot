import telebot
from telebot import types
import random
from random import choice

bot = telebot.TeleBot('6134784688:AAHLgvI7Fyv6pW61-INr-FM4PWkSsyDU82M')

spacefacts = ['я бот...',
              'Мужчины могут воспринимать более мелкие шрифты нежели женщина, при этом у женщин лучше слух',
              'За последние 4000 лет человек не одомашнил ни одного животного.',
              'Взрослый кит за 2 секунды вдыхает 2400 литров воздуха.',
              'Человеческий волос толще мыльной пленки примерно в 5000 раз.',
              'Мужчины чаще страдают инфарктами чем женщины, потому что привыкли все держать в себе.',
              'Запасом своего яда королевская кобра может убить двадцать человек или одного слона',
              'У улитки около 25 000 зубов.',
              'скучный факт',
              'Зоопаpк в Токио каждый год закpывается на 2 месяца, чтобы звеpи могли отдохнyть от посетителей',
              'Взрослый Александр может съесть 3 сосиски за 1 перемену...',
              ]

@bot.message_handler(commands=['start'])  # стартовая команда
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Начать!")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Ну давай начинай!", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Начать!':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn9 = types.KeyboardButton('Рандомный факт')
        btn10 = types.KeyboardButton('🔙 Вернуться в главное менюс')
        markup.add(btn9, btn10)
        bot.send_message(message.from_user.id, 'Выбирай чо хочеш', reply_markup=markup)

    elif message.text == '🔙 Вернуться в главное менюс':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Начать!")
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Ну давай начинай!", reply_markup=markup)


    elif message.text == 'Рандомный факт':
        for i in range(1):
            bot.send_message(message.from_user.id, random.choice(spacefacts))



    # Small talk
    elif message.text == 'Привет!':
        bot.send_message(message.from_user.id, 'qq ;)')

    elif message.text == 'привет!':
        bot.send_message(message.from_user.id, 'q :D')

    elif message.text == 'привет':
        bot.send_message(message.from_user.id, 'qq :)!')

    elif message.text == 'как дела?':
        bot.send_message(message.from_user.id, 'я хочу пиццы, а так хорошо)')

    elif message.text == 'Как дела?':
        bot.send_message(message.from_user.id, 'атлишна!')

    elif message.text == 'Что делаешь?':
        bot.send_message(message.from_user.id, 'Служу Полине')

    elif message.text == 'что делаешь?':
        bot.send_message(message.from_user.id, 'Помогаю своему хозяину')

    elif message.text == 'как дела':
        bot.send_message(message.from_user.id, 'падет...!')

    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Я умею реагировать на привествие и вопрос "как дела", а также могу рассказать факт')



bot.polling(none_stop=True, interval=0)  # обязательная для работы бота часть