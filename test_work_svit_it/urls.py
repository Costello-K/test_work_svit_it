"""SVIT IT URLS Configuration"""
from django.contrib import admin
from django.urls import path, include

from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('user.urls')),
    path('v1/', include('api_v1.urls')),
]

# add the URL patterns for API documentation
urlpatterns += doc_urls
