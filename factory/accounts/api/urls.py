from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import CustomUserViewSet


router = SimpleRouter()
router.register('users', CustomUserViewSet, basename='users')


urlpatterns = [
    path('auth/', include('djoser.urls.authtoken')),
    path('', include(router.urls))
]
