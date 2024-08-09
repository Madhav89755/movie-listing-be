from django.urls import path, include
from .swagger import schema_view
from django.contrib import admin


admin.site.site_title="Movie list Admin"
admin.site.site_header="Movie list Administrator"


urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    path("admin/", admin.site.urls),
    path("collection/", include("collection.urls")),
    path("", include("movies.urls")),
    path("request-count/", include("user_requests.urls"))
]
