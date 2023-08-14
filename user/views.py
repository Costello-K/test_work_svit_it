from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import LoginSerializer


# API view for user login
@api_view(['POST'])              # define HTTP methods allowed for this view
@permission_classes([AllowAny])  # set permissions for this view
def login_view(request):
    """
    Handle user login.

    :param request: HTTP request object {"username":"", "password":""}.
    :return: Response with login status.
    """
    if request.user.is_authenticated:
        return Response({"status": "Already logged in"}, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = request.data.get('username')
            password = request.data.get('password')

            # authenticate user
            user = authenticate(username=username, password=password)
            if user is not None:
                # log in the user
                login(request, user)
                return Response({"status": "Login successful"}, status=status.HTTP_200_OK)
            else:
                return Response({"status": "Login failed"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED) # method not allowed for other HTTP verbs

# API view for user logout
@api_view(['POST'])                     # define HTTP methods allowed for this view
@permission_classes([IsAuthenticated])  # set permissions for this view
def logout_view(request):
    """
    Handle user logout.

    :param request: HTTP request object.
    :return: Response with logout status.
    """
    # log out the user
    logout(request)
    return Response({"status": "Logout successful"}, status=status.HTTP_200_OK)
