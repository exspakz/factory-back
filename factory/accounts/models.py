from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseUser(AbstractUser):
    first_name = models.CharField('first name', max_length=150)

    REQUIRED_FIELDS = ['first_name']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return f'{self._meta.verbose_name}: {self.username}'


class ProxyBaseUser(BaseUser):
    class Meta:
        proxy = True
        app_label = 'auth'
        verbose_name = 'user'
        verbose_name_plural = 'users'


class UserProfile(models.Model):
    telegram_chat_id = models.CharField(
        'telegram chat id', max_length=255, blank=True, null=True
    )
    telegram_token = models.CharField(
        'telegram token', max_length=255, unique=True, blank=True, null=True
    )

    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'user profile'
        verbose_name_plural = 'profiles users'

    def __str__(self):
        return f'{self.user.username}'
