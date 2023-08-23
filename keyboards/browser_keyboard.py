import os
import telebot

browser_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
browser_keyboard.add('Новая вкладка','Закрыть вкладку')
browser_keyboard.add('Открыть ссылку','Закрыть браузер')
browser_keyboard.add('Назад')