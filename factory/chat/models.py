from django.core.validators import MaxLengthValidator
from django.db import models


class Message(models.Model):
    text = models.TextField('text',  validators=[MaxLengthValidator(1000)])
    created_at = models.DateTimeField('date created', auto_now_add=True)

    user = models.ForeignKey(
        'accounts.BaseUser',
        related_name='messages',
        on_delete=models.CASCADE,
        verbose_name='user',
    )

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'

    def __str__(self):
        return f'{self.text[:20]}...'

