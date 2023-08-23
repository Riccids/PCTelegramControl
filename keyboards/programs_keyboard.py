import os
import telebot

programs_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
programs_keyboard.add('Получить системную клавиатуру')
programs_keyboard.add('Получить браузерную клавиатуру')
programs_keyboard.add('Получить программную клавиатуру')