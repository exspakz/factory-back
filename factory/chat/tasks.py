import telebot
from celery import shared_task
from django.conf import settings

bot = telebot.TeleBot(settings.TELEGRAM_TOKEN)


@shared_task
def send_telegram_message(chat_id, text):
    bot.send_message(chat_id, text)
