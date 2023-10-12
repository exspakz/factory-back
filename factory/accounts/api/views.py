from django.contrib.auth.tokens import default_token_generator

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from djoser.views import UserViewSet

from .mixins import ActivationMixin, PasswordMixin, UsernameMixin


class CustomUserViewSet(ActivationMixin, PasswordMixin, UsernameMixin, UserViewSet):
    http_method_names = ['get', 'post', 'delete', 'head', 'options']


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def generate_telegram_token(request):
    profile = request.user.userprofile
    token = default_token_generator.make_token(profile.user)

    profile.telegram_token = token
    profile.save()

    return Response({'telegram_token': token}, status=200)
