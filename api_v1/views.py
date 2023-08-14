from django.contrib.auth import get_user_model
from rest_framework import status, generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status

from services.database import get_all_logs
from .models import Log
from .serializers import (
    FileUploadSerializer,
    LogListSerializer,
)

User = get_user_model()


class FileUploadAPIView(generics.CreateAPIView):
    """Upload file with logs"""
    serializer_class = FileUploadSerializer

    def post(self, request, *args, **kwargs):
        """
        Handle file upload with logs.

        :param request: HTTP request object.
        :return: Response with upload status.
        """
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():  # check if the serializer data is valid
            serializer.save()      # save the uploaded file and associated logs
            return Response({'detail': 'File uploaded successfully.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogListAPIView(generics.ListAPIView):
    """Show list of all logs"""
    serializer_class = LogListSerializer                              # use the LogListSerializer for data representation
    queryset = get_all_logs()                                         # retrieve all logs from the database
    filterset_fields = {
        'user': ['exact'],                                            # filter logs by user (exact match)
        'filename': ['exact', 'icontains'],                           # Filter logs by filename (exact match or case-insensitive substring)
        'datetime_adding_log': ['date', 'date__gte', 'date__lte'],    # Filter logs by adding datetime (date or range)
        'datetime_creating_log': ['date', 'date__gte', 'date__lte'],  # Filter logs by creating datetime (date or range)
    }
    search_fields = ['log']                                           # enable search by log content
