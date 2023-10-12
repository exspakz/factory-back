from rest_framework import serializers
from djoser.serializers import UserCreatePasswordRetypeSerializer

from accounts.models import TelegramData


class CustomUserCreateSerializer(UserCreatePasswordRetypeSerializer):
    def create(self, validated_data):
        user = super().create(validated_data)
        TelegramData.objects.create(user=user)
        return user


class TelegramChatIdSerializer(serializers.Serializer):
    token = serializers.CharField(required=True)
    chat_id = serializers.CharField(required=True)
