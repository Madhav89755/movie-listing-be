from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg.generators import OpenAPISchemaGenerator


class CustomsSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["https", "http"]
        return schema




schema_view = get_schema_view(
    openapi.Info(
        title="Movie Listing API",
        default_version='v1',
        description="Welcome to the Movie List API documentation",
    ),
    generator_class=CustomsSchemaGenerator,
    public=True,
    permission_classes=(permissions.AllowAny,),
)
