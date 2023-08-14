from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.Login.as_view()),
    path('logout/', views.LogoutAPIView.as_view()),
]
