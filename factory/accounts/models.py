from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseUser(AbstractUser):
    first_name = models.CharField('first name', max_length=150)

    REQUIRED_FIELDS = ['first_name']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return f'{self.username}'


class ProxyBaseUser(BaseUser):
    class Meta:
        proxy = True
        app_label = 'auth'
        verbose_name = 'user'
        verbose_name_plural = 'users'


class TelegramData(models.Model):
    chat_id = models.CharField(
        'telegram chat id', max_length=255, blank=True, null=True
    )
    token = models.CharField(
        'telegram token', max_length=255, unique=True, blank=True, null=True
    )

    user = models.OneToOneField(
        BaseUser, on_delete=models.CASCADE, related_name='telegram'
    )

    class Meta:
        verbose_name = 'telegram'
        verbose_name_plural = 'telegram'

    def __str__(self):
        return f'{self.user.username}'
