from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
import pytest

User = get_user_model()


# Test case for successful login
@pytest.mark.django_db
def test_login_success(client):
    # create user
    user = User.objects.create_user(username='testuser', password='testpassword')
    # send a POST request to login
    response = client.post(reverse('login_view'), {'username': 'testuser', 'password': 'testpassword'}, format='json')

    # assertions
    assert response.status_code == status.HTTP_200_OK
    assert 'Login successful' in response.data['status']

# Test case for failed login attempt
@pytest.mark.django_db
def test_login_failure(client):
    # send a POST request to login
    response = client.post(reverse('login_view'), {'username': 'nonexistent', 'password': 'wrongpas'}, format='json')

    # assertions
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'Login failed' in response.data['status']

# Test case for already logged-in user
@pytest.mark.django_db
def test_already_login(client):
    # create user
    user = User.objects.create_user(username='testuser', password='testpassword')
    # send a POST request to login
    response = client.post(reverse('login_view'), {'username': 'testuser', 'password': 'testpassword'}, format='json')
    response = client.post(reverse('login_view'), {'username': 'testuser', 'password': 'testpassword'}, format='json')

    # assertions
    assert response.status_code == status.HTTP_200_OK
    assert 'Already logged in' in response.data['status']

# Test case for logging out
@pytest.mark.django_db
def test_logout(client):
    # create user
    user = User.objects.create_user(username='testuser', password='testpassword')
    # send a POST request to login
    client.login(username='testuser', password='testpassword')
    # send a POST request to logout
    response = client.post(reverse('logout_view'))

    # assertions
    assert response.status_code == status.HTTP_200_OK
    assert 'Logout successful' in response.data['status']