from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Log
from services.parsers import parse_row_to_date_log
from services.archive_extractor.archive_extractor import archive_extractor
from services.database import create_logs_transaction
from services.file_reader.file_reader import file_reader

User = get_user_model()


# Serializer for file upload with logs
class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()  # field for uploading files
    parser = parse_row_to_date_log  # parser function for log date extraction
    reader = file_reader            # function for reading CSV files into a list
    extractor = archive_extractor   # function for extract archive files into a list

    def create(self, validated_data):
        """
        Create logs from the uploaded file.
        """
        user = self.context['request'].user  # get the authenticated user
        file = validated_data.get('file')

        # checking the size of the uploaded file against the maximum allowable file size
        if file.size > (settings.DATA_UPLOAD_MAX_FILE_SIZE_MB * 1024 * 1024):
            raise ValueError(f'Maximum file size allowed is {settings.DATA_UPLOAD_MAX_FILE_SIZE_MB}MB')

        # extract files from the archive
        extracted_files = self.extractor(file)

        # create a list of log objects
        data_logs = []
        for f in extracted_files:
            data_logs.extend(self.reader(f, self.parser))

        # write all the logs to the database in one transaction
        create_logs_transaction(data_logs)

        return file


# Serializer for listing logs
class LogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ['id', 'filename', 'datetime_adding_log', 'datetime_creating_log', 'log']
