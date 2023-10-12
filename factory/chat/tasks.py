import telebot
from django.conf import settings

bot = telebot.TeleBot(settings.TELEGRAM_TOKEN)


def send_telegram_message(chat_id, text):
    bot.send_message(chat_id, text)
