from rest_framework.permissions import AllowAny

from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.views import get_schema_view


DESCRIPTION_API = """This backend application provides a RESTful API for users to 
register, authenticate, and send messages. Upon sending a message via the API, 
the content is immediately forwarded to the user's Telegram via a bot."""


class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["http", "https"]
        return schema


schema_view = get_schema_view(
    openapi.Info(
        title='Factory API',
        default_version='v1',
        description=DESCRIPTION_API,
        terms_of_service='https://factory.ru/terms/',
        contact=openapi.Contact(email='support@factory.ru'),
        license=openapi.License(name='BSD License'),
    ),
    public=True,
    permission_classes=[AllowAny],
    generator_class=BothHttpAndHttpsSchemaGenerator,
)
