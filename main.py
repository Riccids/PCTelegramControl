import comtypes
import os
import telebot
import pybrightness
import tempfile
import pyautogui
import webbrowser
from config import TOKEN
#################################################################################################
from keyboards.main_keyboard import maain_markup
from keyboards.system_keyboard import system_keybpard
from keyboards.browser_keyboard import browser_keyboard
from keyboards.programs_keyboard import programs_keyboard
#################################################################################################
from functions.system import set_volume, set_brightness


bot = telebot.TeleBot(TOKEN)
default_volume = 0.2
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, '🤗', reply_markup= maain_markup)

@bot.message_handler(regexp='назад')
def start(message):
    bot.send_message(message.chat.id, 'Добро пожаловать на главную страницу', reply_markup= maain_markup)

@bot.message_handler(regexp='получить системную')
def show_system_keyboard(message):
    bot.send_message(message.chat.id, 'Системная клавиатура', reply_markup=system_keybpard)

@bot.message_handler(regexp='получить браузерную')
def show_system_keyboard(message):
    bot.send_message(message.chat.id, 'Браузерная клавиатура', reply_markup=browser_keyboard)

@bot.message_handler(regexp='получить программную')
def show_system_keyboard(message):
    bot.send_message(message.chat.id, 'Программная клавиатура', reply_markup=programs_keyboard)

@bot.message_handler(regexp='выключить')
def echo_message(message):
    bot.send_message(message.chat.id, 'Выключение...')
    try:
        bot.send_message(message.chat.id, 'Устройство выключено...')
        os.system("shutdown -s -t 0")
    except:
        bot.send_message(message.chat.id, 'Произошла непредвиденная ошибка')

@bot.message_handler(regexp='Повысить громкость')
def echo_message(message):
    comtypes.CoInitialize()
    set_volume(0.7)
    comtypes.CoUninitialize()
    bot.send_message(message.chat.id, 'Изменено')


@bot.message_handler(regexp='Понизить громкость')
def echo_message(message):
    comtypes.CoInitialize()
    set_volume(0.5)
    comtypes.CoUninitialize()
    bot.send_message(message.chat.id, 'Изменено')    

@bot.message_handler(regexp='Повысить яркость')
def echo_message(message):
    comtypes.CoInitialize()
    pybrightness.custom(percent=98)
    comtypes.CoUninitialize()
    bot.send_message(message.chat.id, 'Изменено')

@bot.message_handler(regexp='Понизить яркость')
def echo_message(message):
    comtypes.CoInitialize()
    pybrightness.custom(percent=70)
    comtypes.CoUninitialize()
    bot.send_message(message.chat.id, 'Изменено')


@bot.message_handler(regexp='новая')
def echo_message(message):
    url = 'ya.ru'
    webbrowser.open_new_tab(url)
    bot.send_message(message.chat.id, 'Открыта новая вкладка')

@bot.message_handler(regexp='закрыть вкладку')
def echo_message(message):
    pyautogui.hotkey('ctrl','w')
    bot.reply_to(message, 'Вкладка успешно закрыта')

@bot.message_handler(regexp='открыть')
def open_url(message):
    bot.reply_to(message, 'Введите ссылку:')
    bot.register_next_step_handler(message, process_url)
def process_url(message):
    url = message.text.strip()
    # Проверка введенной ссылки
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'http://' + url
    try:
        # Открытие ссылки в браузере
        webbrowser.open_new_tab(url)
        bot.reply_to(message, f'Открыта ссылка: {url}')
    except Exception as e:
        bot.reply_to(message, f'Ошибка при открытии ссылки: {str(e)}')

@bot.message_handler(regexp='браузер')
def echo_message(message):
    pyautogui.hotkey('alt', 'F4')
    bot.reply_to(message, 'Браузер закрыт')
# @bot.message_handler(regexp='получить скриншот')
# def echo_meesage(message):
#     path = tempfile.gettempdir() + 'screenshot.png'
#     screenshot = ImageGrab.grab()
#     screenshot.save(path, 'PNG')
#     bot.send_photo(message.chat.id, open(path, 'rb'))

# @bot.message_handler(regexp='перезапустить') #вызов по команде /restart; можно сделать и на кнопку
# def restart(message):
#   try:
#       bot.send_message(message.chat.id, 'Успешная перезагрузка бота')
#       pid = str(os.getpid()) #получаем ProcessID запущенного бота
#       restarter = open('restarter.bat', 'w') #открываем/создаем батник
#       restarter.write('Taskkill /PID ' + pid + ' /F\nTIMEOUT /T 5 /NOBREAK\ncd D:\\Repos\\py\\PCControlBot\\\nmain.py') #записываем скрипт в батник		
#       restarter.close() #закрываем отредактированный батник
#       os.system('D:/Repos/py/PCControlBot/restarter.bat') #запускаем наш батник
#   except:
#       bot.send_message(message.chat.id, 'Ошибка перезагрузки')


bot.infinity_polling()

