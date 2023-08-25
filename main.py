import comtypes
import os
import telebot
from telebot import types
import pybrightness
import tempfile
import pyautogui
import webbrowser
import subprocess
from PIL import ImageGrab
from config import TOKEN, OPENAI_TOKEN
#################################################################################################
from keyboards.main_keyboard import maain_markup
from keyboards.system_keyboard import system_keybpard
from keyboards.browser_keyboard import browser_keyboard
from keyboards.programs_keyboard import programs_keyboard
from keyboards.youtube_keyboard import youtube_keyboard, pause_video, video_back, video_forward, next_video
from keyboards.social_keyboard import social_keyboard
#################################################################################################
from functions.system import set_volume, set_brightness
from functions.system_information import *



default_volume = 0.2
keyboard = types.InlineKeyboardMarkup()
back_button = types.InlineKeyboardButton('Назад', callback_data='back')
keyboard.add(back_button)



def create_file():
    code = input("Введите код: ")
    with open("code.txt", "w") as file:
        file.write(code)

def read_file():
    if os.path.exists("code.txt"):
        with open("code.txt", "r") as file:
            code = file.read()
            return code
    else:
        return None

code = read_file()
if code is None:
    create_file()
else:
        print("Найден код в файле:")
        print(code)

bot = telebot.TeleBot(token=code)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, '🤗', reply_markup= maain_markup)

@bot.message_handler(commands=['add_app'])
def add_app(message):
    msg = bot.send_message(message.chat.id, "Введите имя приложения и путь к нему в формате 'Имя_приложения Путь_к_приложению':")
    bot.register_next_step_handler(msg, save_app)

def save_app(message):
    try:
        app_data = message.text.split()
        app_name = app_data[0]
        app_path = ' '.join(app_data[1:])
        
        with open('apps.txt', 'a') as file:
            file.write(app_name + '\n')
            file.write(app_path + '\n')
        
        bot.send_message(message.chat.id, f"Приложение {app_name} успешно добавлено!")
    except:
        bot.send_message(message.chat.id, "Что-то пошло не так. Пожалуйста, попробуйте снова.")

@bot.message_handler(commands=['run_app'])
def run_app(message):
    program_name = bot.send_message(message.chat.id, "Введите имя приложения, которое хотите запустить:")
    bot.register_next_step_handler(program_name, process_program_name)
def process_program_name(message):
    program_name = message.text
    with open('apps.txt', 'r') as file:
        lines = file.readlines()

    for i in range(len(lines)):
        if lines[i].strip() == program_name:
            if i+1 < len(lines):
                program_path = lines[i+1].strip()
                try:
                    subprocess.Popen(program_path)
                    print(f"Программа '{program_name}' успешно запущена.")
                except OSError as e:
                    print(f"Ошибка при запуске программы '{program_name}': {e}")
            else:
                print(f"Не удалось найти путь для программы '{program_name}'.")
            break
    else:
        print(f"Программа '{program_name}' не найдена в файле.")

    bot.send_message(message.chat.id, "Ваше приложение успешно запущено!")


@bot.message_handler(commands=['my_apps'])
def show_my_apps(message):
    with open('apps.txt', 'r') as file:
        lines = file.readlines()

    # Создаем список для хранения найденных приложений пользователя
    user_apps = []

    for i in range(len(lines)):
        # Проверяем, является ли индекс строки нечетным числом
        if i % 2 != 0:
            continue

        # Получаем имя приложения
        app_name = lines[i].strip()
        user_apps.append(app_name)

    if user_apps:
        # Формируем сообщение с приложениями пользователя, разделяя их переводом строки
        apps_message = "\n".join(user_apps)
        bot.send_message(message.chat.id, f"Ваши приложения:\n{apps_message}")
    else:
        bot.send_message(message.chat.id, "У вас нет зарегистрированных приложений.")

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

################################################SYSTEM##################################################
@bot.message_handler(regexp='выключить')
def echo_message(message):
    bot.send_message(message.chat.id, 'Выключение...')
    try:
        bot.send_message(message.chat.id, 'Устройство выключено...')
        os.system("shutdown -s -t 0")
    except:
        bot.send_message(message.chat.id, 'Произошла непредвиденная ошибка')

@bot.message_handler(regexp='Изменить громкость')
def echo_message(message):
    bot.reply_to(message, 'Введите число, которому должна соответствовать текущая громкость:')
    bot.register_next_step_handler(message, process)
def process(message):
    try:
        volume = float(float(message.text) / 100)
        comtypes.CoInitialize()
        set_volume(volume)
        comtypes.CoUninitialize()
        bot.send_message(message.chat.id, 'Изменено')
    except Exception as e:
        bot.send_message(message.chat.id, f'Ошибка: {str(e)}')

@bot.message_handler(regexp='Изменить яркость')
def echo_message(message):
    bot.reply_to(message, 'Введите число, которому должна соответствовать текущая яркость:')
    bot.register_next_step_handler(message, process)
def process(message):
    try:
        brightness = int(message.text)
        comtypes.CoInitialize()
        pybrightness.custom(percent=brightness)
        comtypes.CoUninitialize()
        bot.send_message(message.chat.id, 'Изменено')
    except Exception as e:
        bot.send_message(message.chat.id, f'Ошибка: {str(e)}') 

@bot.message_handler(regexp='о системе')
def echo_message(message):
    get_system_information(bot,message)
    get_cpu_inforamtion(bot,message)
    get_disk_usage(bot,message)

######################################################BROWSER#############################################################

@bot.message_handler(regexp='Поиск по')
def echo_message(message):
    bot.reply_to(message, 'Введите запрос, который хотите отобразить на ютубе')
    bot.register_next_step_handler(message, search_youtube)
def search_youtube(message):
    youtube_url = message.text.replace(' ','+')
    # Проверка введенной ссылки
    if not youtube_url.startswith('https://www.youtube.com/results?search_query='):
        youtube_url = 'https://www.youtube.com/results?search_query=' + youtube_url
    try:
        bot.send_message(message.chat.id,'Обработка запроса...',reply_markup=youtube_keyboard)
        # Открытие ссылки в браузере
        webbrowser.open_new_tab(youtube_url)
        bot.reply_to(message, f'Выполнен поиск по вашему запросу')
        path = tempfile.gettempdir() + 'screenshot.png'
        screenshot = ImageGrab.grab()
        screenshot.save(path, 'PNG')
        bot.send_photo(message.chat.id, open(path, 'rb'))
    except Exception as e:
        bot.reply_to(message, f'Ошибка при открытии ссылки: {str(e)}')

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
        if 'youtube' in url:
            bot.send_message(message.chat.id,'Обработка запроса...',reply_markup=youtube_keyboard)
        # Открытие ссылки в браузере
        webbrowser.open_new_tab(url)
        bot.reply_to(message, f'Открыта ссылка: {url}')
    except Exception as e:
        bot.reply_to(message, f'Ошибка при открытии ссылки: {str(e)}')

@bot.message_handler(regexp='браузер')
def echo_message(message):
    pyautogui.hotkey('alt', 'F4')
    bot.reply_to(message, 'Браузер закрыт')

@bot.message_handler(regexp='соц.')
def echo_message(message):
    bot.send_message(message.chat.id, 'Клавиатура для соц. сетей', reply_markup=social_keyboard)

@bot.message_handler(regexp='VK')
def echo_message(message):
    webbrowser.open_new_tab('vk.com')
    bot.reply_to(message, 'Ссылка успешно открыта в новой вкладке')

@bot.message_handler(regexp='Telegram')
def echo_message(message):
    webbrowser.open_new_tab('web.telegram.org')
    bot.reply_to(message, 'Ссылка успешно открыта в новой вкладке')

@bot.message_handler(regexp='Instagram')
def echo_message(message):
    webbrowser.open_new_tab('instagram.com')
    bot.reply_to(message, 'Ссылка успешно открыта в новой вкладке')

@bot.message_handler(regexp='Twitter')
def echo_message(message):
    webbrowser.open_new_tab('twitter.com')
    bot.reply_to(message, 'Ссылка успешно открыта в новой вкладке')


###################################YOUTUBE############################################################################################
@bot.message_handler(regexp='>>')
def echo_message(message):
    video_forward(bot,message)

@bot.message_handler(regexp='<<')
def echo_message(message):
    video_back(bot, message)

@bot.message_handler(regexp='следующее видео')
def echo_message(message):
    next_video(bot, message)

##################################ДЕЙСТВИЯ С ЭКРАНОМ#######################################
@bot.message_handler(regexp='получить скриншот')
def echo_meesage(message):
    path = tempfile.gettempdir() + 'screenshot.png'
    screenshot = ImageGrab.grab()
    screenshot.save(path, 'PNG')
    bot.send_photo(message.chat.id, open(path, 'rb'))


@bot.message_handler(regexp='||')
def echo_message(message):
    pause_video(bot,message)


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

