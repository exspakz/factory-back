from django.contrib.auth.tokens import default_token_generator

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from djoser.views import UserViewSet

from accounts.models import TelegramData
from .mixins import ActivationMixin, PasswordMixin, UsernameMixin
from .serializers import TelegramChatIdSerializer


class CustomUserViewSet(ActivationMixin, PasswordMixin, UsernameMixin, UserViewSet):
    http_method_names = ['get', 'post', 'delete', 'head', 'options']


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def generate_telegram_token(request):
    user_telegram = request.user.telegram
    token = default_token_generator.make_token(user_telegram.user)

    user_telegram.token = token
    user_telegram.save()

    return Response({'telegram_token': token}, status=200)


@api_view(['POST'])
def save_telegram_chat_id(request):
    serializer = TelegramChatIdSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=400)

    token = serializer.validated_data['token']
    chat_id = serializer.validated_data['chat_id']

    try:
        user_telegram = TelegramData.objects.get(token=token)
        user_telegram.chat_id = chat_id
        user_telegram.save()
        return Response({'detail': 'Chat ID saved successfully.'}, status=200)
    except TelegramData.DoesNotExist:
        return Response({'detail': 'Invalid token.'}, status=400)
