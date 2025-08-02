from django.contrib import admin
from django.urls import path, re_path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.shortcuts import redirect
schema_view = get_schema_view(
    openapi.Info(
        title="Book API",
        default_version='v1',
        description="API for my book recommender",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path('', lambda request: redirect('schema-swagger-ui', permanent=False)),
    path('admin/', admin.site.urls),
    path('api/', include('library.urls')),  # all your API endpoints
# Swagger UI
    # Swagger UI
    re_path(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # ReDoc UI
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]