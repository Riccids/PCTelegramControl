import os
import telebot

maain_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
maain_markup.add('Получить системную клавиатуру')
maain_markup.add('Получить браузерную клавиатуру')
maain_markup.add('Получить программную клавиатуру')