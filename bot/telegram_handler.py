import telebot
from . import config, qbittorrent_client
from functools import wraps
from . import config

bot = telebot.TeleBot(config.TELEGRAM_API_KEY)
client = qbittorrent_client.connect_client()


def authorized_only(func):
    @wraps(func)
    def wrapper(message, *args, **kwargs):
        if message.from_user.id not in config.ALLOWED_USER_IDS:
            bot.reply_to(message, "\u26d4 You are not authorized to use this bot.")
            return
        return func(message, *args, **kwargs)
    return wrapper

@bot.message_handler(commands=['start'])
@authorized_only
def start(message):
    bot.reply_to(message, "Ahoy sailor, lets sail the high seas.")

@bot.message_handler(commands=['add'])
@authorized_only
def add(message):
    try:
        magnet = message.text.split(" ", 1)[1]
        qbittorrent_client.add_torrent(client, magnet)
        bot.reply_to(message, "Torrent added ✅")
    except IndexError:
        bot.reply_to(message, "Usage: /add <magnet link>")

@bot.message_handler(commands=['status'])
@authorized_only
def status(message):
    status_list = qbittorrent_client.get_status(client)
    if not status_list:
        bot.reply_to(message, "No active torrents.")
        return
    reply = "\n".join([f"{name} - {state} ({progress}%)" for name, state, progress in status_list])
    bot.reply_to(message, reply)

def run():
    bot.polling()

