from __future__ import annotations

from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework.response import Response

from .serializers import LoginSerializer
from .serializers import RegisterSerializer
from core_viewsets.custom_viewsets import CreateViewSet
from core_viewsets.custom_viewsets import ListViewSet

# Create your views here.


class RegisterViewSet(CreateViewSet):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = RegisterSerializer
    queryset = get_user_model().objects.all()

    def create(self, request, *args, **kwargs):

        email = request.data.get('email')
        password = request.data.get('password', None)
        phone_number = request.data.get('phone_number')

        # TODO: Validations (Example: Check if email or phone number already exists)
        if get_user_model().objects.filter(email=email).exists():
            return Response({'code': 400, 'message': 'Email already exists'})

        user = get_user_model().objects.create_user(request.data)

        return Response(
            {'code': 200, 'message': 'success', 'user_id': user._get_pk_val()},
        )

from rest_framework import status
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class LoginViewSet(CreateViewSet):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
         # Authenticate the user
        user = get_user_model().objects.filter(email=email).first()

        if user and user.check_password(password):
            # Update last login time
            user.last_login = timezone.now()
            user.save()

            # Generate JWT tokens
            payload = jwt_payload_handler(user)
            access_token = jwt_encode_handler(payload)


            return Response(
                {
                    'code': 200,
                    'message': 'success',
                    'access_token': access_token,
                    'refresh_token': 'refresh_token',
                    'user_id': user.pk,
                    'name': user.first_name,
                    'email': user.email,
                    'last_login': user.last_login,
                }, status=status.HTTP_200_OK)
        else:
            return Response({
                'code': 401,
                'message': 'Invalid credentials'
            }, status=status.HTTP_401_UNAUTHORIZED)
        


class MeViewSet(ListViewSet):
    authentication_classes = ()  # ToDO Specify Auth class
    permission_classes = ()
    serializer_class = None  # ToDO Specify serializer_class class
    queryset = get_user_model().objects.all()

    def list(self, request, *args, **kwargs):
        # ToDO:  Add your code
        return Response({})
