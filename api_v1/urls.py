from django.urls import path

from . import views

urlpatterns = [
    path('files/upload/', views.FileUploadAPIView.as_view(), name='file_upload'),
    path('logs/', views.LogListAPIView.as_view(), name='logs'),
]
