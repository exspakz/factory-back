from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import ProxyBaseUser, UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'telegram_chat_id',
        'telegram_token',
    )
    list_display_links = ('id', 'user')
    search_fields = ('user__username',)


admin.site.register(ProxyBaseUser, UserAdmin)
