from djoser.views import UserViewSet

from .mixins import ActivationMixin, PasswordMixin, UsernameMixin


class CustomUserViewSet(ActivationMixin, PasswordMixin, UsernameMixin, UserViewSet):
    http_method_names = ['get', 'post', 'delete', 'head', 'options']

