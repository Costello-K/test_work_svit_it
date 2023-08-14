from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.db.models import Q

from .models import Log

User = get_user_model()


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

    def parse_log_row(self, row):
        if len(row) >= 2:
            datetime_creating_log_str = row[0]
            log_text = row[1]
        else:
            raise ValueError('111')

        try:
            datetime_creating_log = datetime.strptime(datetime_creating_log_str, '%Y-%m-%d %H:%M:%S,%f')
        except ValueError:
            datetime_creating_log = timezone.now()

        return {
            'datetime_creating_log': datetime_creating_log,
            'log': log_text
        }

    def create(self, validated_data):
        user = self.context['request'].user
        file = validated_data['file']

        logs_created = []
        with open(file.temporary_file_path(), 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                log_data = self.parse_log_row(row)
                log_data['user'] = user
                log_data['filename'] = file.name

                logs_created.append(Log.objects.create(**log_data))

        return logs_created


class LogsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ['id', 'filename', 'datetime_adding_log', 'datetime_creating_log', 'log']
