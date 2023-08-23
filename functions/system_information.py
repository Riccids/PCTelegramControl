import psutil
import platform
from datetime import datetime
import telebot
from config import TOKEN

bot = telebot.TeleBot(token =TOKEN)

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def get_system_information(bot,message):
    bot.send_message(message.chat.id,'====System Information==== ')
    uname = platform.uname()
    bot.send_message(message.chat.id,f"System: {uname.system}")
    bot.send_message(message.chat.id,f"Node Name: {uname.node}")
    bot.send_message(message.chat.id,f"Release: {uname.release}")
    bot.send_message(message.chat.id,f"Version: {uname.version}")
    bot.send_message(message.chat.id,f"Machine: {uname.machine}")
    bot.send_message(message.chat.id,f"Processor: {uname.processor}")

def get_cpu_inforamtion(bot,message):
    bot.send_message(message.chat.id,"====CPU Info====")
    # number of cores
    bot.send_message(message.chat.id,f"Physical cores:{psutil.cpu_count(logical=False)}")
    bot.send_message(message.chat.id,f"Total cores:{psutil.cpu_count(logical=True)}")
    # CPU frequencies
    cpufreq = psutil.cpu_freq()
    bot.send_message(message.chat.id,f"Max Frequency: {cpufreq.max:.2f}Mhz")
    bot.send_message(message.chat.id,f"Min Frequency: {cpufreq.min:.2f}Mhz")
    bot.send_message(message.chat.id,f"Current Frequency: {cpufreq.current:.2f}Mhz")
    # CPU usage
    bot.send_message(message.chat.id,"CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        bot.send_message(message.chat.id,f"Core {i}: {percentage}%")
    bot.send_message(message.chat.id,f"Total CPU Usage: {psutil.cpu_percent()}%")

def get_disk_usage(bot,message):
    bot.send_message(message.chat.id,"====Disk Information====")
    bot.send_message(message.chat.id,"Partitions and Usage:")
    # get all disk partitions
    partitions = psutil.disk_partitions()
    for partition in partitions:
        bot.send_message(message.chat.id,f"=== Device: {partition.device} ===")
        bot.send_message(message.chat.id,f"  Mountpoint: {partition.mountpoint}")
        bot.send_message(message.chat.id,f"  File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
        # this can be catched due to the disk that
        # isn't ready
            continue
    bot.send_message(message.chat.id,f"  Total Size: {get_size(partition_usage.total)}")
    bot.send_message(message.chat.id,f"  Used: {get_size(partition_usage.used)}")
    bot.send_message(message.chat.id,f"  Free: {get_size(partition_usage.free)}")
    bot.send_message(message.chat.id,f"  Percentage: {partition_usage.percent}%")
    # get IO statistics since boot
    disk_io = psutil.disk_io_counters()
    bot.send_message(message.chat.id,f"Total read: {get_size(disk_io.read_bytes)}")
    bot.send_message(message.chat.id,f"Total write: {get_size(disk_io.write_bytes)}")

