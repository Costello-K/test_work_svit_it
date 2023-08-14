from django.conf import settings
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
import pytest
import os
from zipfile import ZipFile
from io import BytesIO
from datetime import datetime
from dateutil.parser import parse

from api_v1.models import Log

User = get_user_model()


# Test case to upload a CSV file using the API view
@pytest.mark.django_db
def test_csv_file_upload_api_view():
    # create user
    user = User.objects.create_user(username='testuser', password='testpassword')
    client = APIClient()
    # authorize the user
    client.force_login(user)

    # create csv log file
    file_content = (
        b"2023-08-11 10:00:00.000+03,Log content 1\n"
        b"2023-08-11 11:00:00.000+03,Log content 2\n"
    )
    file = BytesIO(file_content)
    file.name = 'example.csv'

    # Send a POST request to upload the file
    response = client.post(reverse('file_upload'), {'file': file}, format='multipart')

    assert response.status_code == status.HTTP_201_CREATED
    assert Log.objects.count() == 2
    assert response.data == {'detail': 'File uploaded successfully.'}

# Similar test cases for uploading different types of compressed files (ZIP, 7z)
@pytest.mark.django_db
def test_zip_csv_file_upload_api_view():
    # create user
    user = User.objects.create_user(username='testuser', password='testpassword')
    client = APIClient()
    # authorize the user
    client.force_login(user)

    # specify the path to the archive
    file_path = os.path.join(settings.BASE_DIR, 'test_work_svit_it/tests/test.zip')
    # send a POST request to upload the file
    response = client.post(reverse('file_upload'), {'file': open(file_path, 'rb')}, format='multipart')

    # assertions
    assert response.status_code == status.HTTP_201_CREATED
    assert Log.objects.count() == 8
    assert response.data == {'detail': 'File uploaded successfully.'}

@pytest.mark.django_db
def test_sevenzip_csv_file_upload_api_view():
    # create user
    user = User.objects.create_user(username='testuser', password='testpassword')
    client = APIClient()
    # authorize the user
    client.force_login(user)

    # specify the path to the archive
    file_path = os.path.join(settings.BASE_DIR, 'test_work_svit_it/tests/test.7z')
    # send a POST request to upload the file
    response = client.post(reverse('file_upload'), {'file': open(file_path, 'rb')}, format='multipart')

    # assertions
    assert response.status_code == status.HTTP_201_CREATED
    assert Log.objects.count() == 8
    assert response.data == {'detail': 'File uploaded successfully.'}

# Test case to retrieve a list of logs using the API view
@pytest.mark.django_db
def test_log_list_api_view():
    # create user
    user = User.objects.create_user(username='testuser', password='testpassword')
    client = APIClient()
    # authorize the user
    client.force_login(user)

    # create a log
    Log.objects.create(
        user=user,
        filename='log1.csv',
        datetime_creating_log=parse('2026-08-11 12:00:00.000+04'),
        log='Log content 1'
    )

    # send a GET request to retrieve the list of logs
    response = client.get(reverse('logs'))

    # assertions
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == 1
    assert response.data['results'][0]['filename'] == 'log1.csv'
    assert response.data['results'][0]['log'] == 'Log content 1'

@pytest.mark.django_db
def test_log_list_not_access_api_view():
    # create user
    user = User.objects.create_user(username='testuser', password='testpassword')
    client = APIClient()

    # create a log
    Log.objects.create(
        user=user,
        filename='log1.csv',
        datetime_creating_log=parse('2026-08-11 12:00:00.000+04'),
        log='Log content 1'
    )

    # send a POST request to upload the file
    response = client.get(reverse('logs'))

    # assertions
    assert response.status_code == status.HTTP_403_FORBIDDEN
