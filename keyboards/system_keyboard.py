import os
import telebot

system_keybpard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
system_keybpard.add('Выключить компьютер')
system_keybpard.add('Повысить громкость')
system_keybpard.add('Понизить громкость')
system_keybpard.add('Повысить яркость')
system_keybpard.add('Понизить яркость')