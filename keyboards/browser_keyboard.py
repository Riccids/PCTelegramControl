import os
import telebot

browser_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
browser_keyboard.add('Новая вкладка')
browser_keyboard.add('Закрыть вкладку')
browser_keyboard.add('Открыть ссылку')
browser_keyboard.add('Закрыть браузер')