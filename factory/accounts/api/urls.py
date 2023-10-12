from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import CustomUserViewSet, generate_telegram_token


router = SimpleRouter()
router.register('users', CustomUserViewSet, basename='users')


urlpatterns = [
    path('auth/', include('djoser.urls.authtoken')),
    path('telegram/token/', generate_telegram_token),
    path('', include(router.urls))
]
