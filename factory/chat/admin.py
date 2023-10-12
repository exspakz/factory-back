from django.contrib import admin

from . import models


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'user')
    list_display_links = ('id', 'text')
    search_fields = ['user', 'text']
