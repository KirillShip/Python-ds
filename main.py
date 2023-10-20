import telebot
from telebot import types
import re

TOKEN = '6447996107:AAFMcuJPDWTOi2zUFdA_hNOpUGh-dV5a4wQ'

bot = telebot.TeleBot(TOKEN)

phone_number_regex = re.compile(r'^(\+7|8)\d{10}$')
name_regex = re.compile(r'^[А-ЯЁ][а-яё]+\s[А-ЯЁ][а-яё]+(\s[А-ЯЁ][а-яё]+)?$')
name = ''
phone_number = ''

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Пожалуйста, введите свой номер телефона и ФИО в разных сообщениях для записи")
    
# Обработчик текстовых сообщений
@bot.message_handler(content_types=['text'])
def handle_text(message):
    global name
    global phone_number
    if message.text.startswith('/start'):
        return
    if message.text.startswith('/getID'):
        bot.send_message(message.chat.id, message.chat.id)
        return
    if message.text.startswith('/'):
        bot.send_message(message.chat.id, 'Неверная команда')
        return
    if phone_number_regex.match(message.text):
        bot.send_message(message.chat.id, 'Вы успешно ввели номер телефона')
        phone_number = message.text
        if (name != '' and phone_number != ''):
            bot.send_message(-4023403322, f'Имя: {name}\nТелефон: {phone_number}')
            bot.send_message(message.chat.id, 'Вы успешно записались на пробное занятие. С вами свяжется наш менеджер')
        return
    if name_regex.match(message.text):
        bot.send_message(message.chat.id, 'Вы успешно ввели Ваше ФИО')
        name = message.text
        if (name != '' and phone_number != ''):
            bot.send_message(-4023403322, f'Имя: {name}\nТелефон: {phone_number}')
            bot.send_message(message.chat.id, 'Вы успешно записались на пробное занятие. С вами свяжется наш менеджер')
        return
    else:
        bot.send_message(message.chat.id, 'Повторите попытку')
        return

bot.infinity_polling()
