from django.urls import path

from . import views

urlpatterns = [
    path('files/upload/', views.FileUploadAPIView.as_view()),
    path('logs/', views.LogsListAPIView.as_view()),
]