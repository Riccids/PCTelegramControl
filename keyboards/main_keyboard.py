import os
import telebot

maain_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
maain_markup.add('Получить системную клавиатуру')
maain_markup.add('Получить браузерную клавиатуру')
maain_markup.add('Получить программную клавиатуру')
maain_markup.add('Получить информацию о системе')
maain_markup.add('Получить скриншот текущего рабочего стола')