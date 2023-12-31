from django.contrib import admin
from django.urls import path, include

from .api_docs_config import schema_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include('accounts.api.urls')),
    path('', include('chat.api.urls')),
]
