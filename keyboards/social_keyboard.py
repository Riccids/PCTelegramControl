import os
import telebot

social_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
social_keyboard.add('VK','Telegram')
social_keyboard.add('Instagram','Twitter')
social_keyboard.add('Поиск по Youtube')
social_keyboard.add('Назад')