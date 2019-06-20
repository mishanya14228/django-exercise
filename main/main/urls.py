"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url

from drfpasswordless.views import (
    ObtainEmailCallbackToken,
    ObtainAuthTokenFromCallbackToken,
)


schema_view = get_schema_view(
    openapi.Info(
       title="Django Exercise API",
       default_version='v1',
       description="Docs for Django Exercise",
       terms_of_service="https://www.google.com/policies/terms/",
       contact=openapi.Contact(email="contact@djangoexercise.local"),
       license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

drfpasswordless_patterns = [
    path('callback/auth/', ObtainAuthTokenFromCallbackToken.as_view(),
         name='auth_callback'),
    path('auth/email/', ObtainEmailCallbackToken.as_view(), name='auth_email'),
]

urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),
    path('schema/', schema_view),  # for the schema
    path('admin/', admin.site.urls),
    path('api/v1/', include('django.contrib.auth.urls')),  # added auth urls
    path('api/v1/', include(drfpasswordless_patterns)),  # for passwordless
    path('api/v1/', include('api.urls')),  # Added url for api app
]
