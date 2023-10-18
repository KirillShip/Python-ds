import telebot
from telebot import types

TOKEN = '6447996107:AAFMcuJPDWTOi2zUFdA_hNOpUGh-dV5a4wQ'

bot = telebot.TeleBot(TOKEN)

stage = 0

@bot.message_handler(commands=['startquest'])
def start_quest(message):
  markup = types.InlineKeyboardMarkup()
  itembtn1 = types.InlineKeyboardButton(text='Преодолевать желание зайти в лес и попытаться обойти его', callback_data='Вариант 1')
  itembtn2 = types.InlineKeyboardButton(text='Пойти вглубь леса', callback_data='Вариант 2')
  markup.add(itembtn1, itembtn2)
  bot.send_message(message.chat.id, "Вы просыпаетесь на окраине леса и не понимаете как здесь оказались. Вы думаете, что нужно как-то вернуться домой, но что-то притягивает вас вглубь зарослей.", reply_markup=markup)

def quest_stage1(message, variant):
  pass

def quest_stage2(message, variant):
  pass

def quest_stage3(message, variant):
  pass

def quest_stage4(message, variant):
  pass

def quest_stage5(message, variant):
  pass

@bot.callback_query_handler(func=lambda call: True)
def answering(call):
  if stage == 0:
    quest_stage1(call.message, call.data)
  elif stage == 1:
    quest_stage2(call.message, call.data)
  elif stage == 2:
    quest_stage3(call.message, call.data)
  elif stage == 3:
    quest_stage4(call.message, call.data)
  elif stage == 4:
    quest_stage5(call.message, call.data)

    
bot.infinity_polling()