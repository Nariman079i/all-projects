from urllib.request import urlopen

from telebot import TeleBot

from app import settings

bot = TeleBot(token="6216280419:AAFgjYvowwSz81v8rX6VjeKsPtwoJ4p0zn8")


def send_telegram_message(message):
    chat_id = '-872299364'
    bot.send_message(chat_id, message, parse_mode='Markdown')
