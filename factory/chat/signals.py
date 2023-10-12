from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Message
from .tasks import send_telegram_message


@receiver(post_save, sender=Message)
def message_created(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        if chat_id := user.telegram.chat_id:
            text = f'{user.first_name.capitalize()}, я получил от тебя сообщение:\n"{instance.text}"'
            send_telegram_message.delay(chat_id, text)
