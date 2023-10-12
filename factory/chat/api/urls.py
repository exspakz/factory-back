from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import MessageViewSet


router = SimpleRouter()
router.register('messages', MessageViewSet, basename='messages')


urlpatterns = [
    path('', include(router.urls))
]
