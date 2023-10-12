from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated

from chat.api import serializers
from chat.api.permissions import CurrentUserOrAdmin
from chat.models import Message


class MessageViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'delete', 'head', 'options']

    serializer_class = serializers.MessageSerializer
    queryset = Message.objects.all()
    permission_classes = [CurrentUserOrAdmin]

    def permission_denied(self, request, **kwargs):
        if request.user.is_authenticated and self.action in [
            'update',
            'partial_update',
            'list',
            'retrieve',
        ]:
            raise NotFound()
        super().permission_denied(request, **kwargs)

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()
        if self.action == "list" and not user.is_staff:
            queryset = queryset.filter(user=user)
        return queryset

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated]
        elif self.action == 'list':
            self.permission_classes = [CurrentUserOrAdmin]
        elif self.action == 'destroy':
            self.permission_classes = [CurrentUserOrAdmin]
        return super().get_permissions()
