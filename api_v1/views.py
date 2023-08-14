from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import status, generics, permissions

from .models import Log
from .serializers import (
    FileUploadSerializer,
    LogsListSerializer,
)

User = get_user_model()

# Create your views here.
class PostListAPIView(generics.RetrieveAPIView):
    """Upload file with logs"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FileUploadSerializer


class PostListAPIView(generics.ListAPIView):
    """Show list of all logs"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LogsListSerializer
    queryset = Log.objects.all()
    filterset_fields = ['datetime_creating_log', 'log']
    search_fields = ['datetime_creating_log', 'log']
