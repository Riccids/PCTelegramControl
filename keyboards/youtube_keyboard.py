import telebot
import pyautogui
from config import TOKEN
youtube_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
youtube_keyboard.add('▷/||')
youtube_keyboard.add('Перемотать >>')
youtube_keyboard.add('Перемотать <<')
youtube_keyboard.add('Следующее видео ')

bot = telebot.TeleBot(token=TOKEN)

def pause_video(bot, meesage):
    pyautogui.press('space')
    bot.send_message(meesage.chat.id, 'Видео остановлено')


def video_forward(bot, message):
    pyautogui.press('right')
    bot.send_message(message.chat.id, 'Выполнена перемотка вперед на 5 сек.')


def video_back(bot, message):
    pyautogui.press('left')
    bot.send_message(message.chat.id, 'Выполнена перемотка назад на 5 сек.')


def next_video(bot, message):
    pyautogui.hotkey('shift', 'n')
    bot.send_message(message.chat.id, 'Вклюаю следующее видео')
