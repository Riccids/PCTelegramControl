import os
import telebot

system_keybpard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
system_keybpard.add('Выключить компьютер')
system_keybpard.add('Изменить громкость')
system_keybpard.add('Изменить яркость')
