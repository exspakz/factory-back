from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import ProxyBaseUser, TelegramData


@admin.register(TelegramData)
class TelegramDataAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'chat_id',
        'token',
    )
    list_display_links = ('id', 'user')
    search_fields = ('user__username',)


admin.site.register(ProxyBaseUser, UserAdmin)
