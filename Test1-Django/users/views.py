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

        # TODO: Validations

        user = get_user_model().objects.create_user(request.data)

        return Response(
            {'code': 200, 'message': 'success', 'user_id': user._get_pk_val()},
        )


class LoginViewSet(CreateViewSet):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        # TODO: validation
        user_obj = get_user_model().objects.get(email=email, password=password)
        # TODO:  generate token with jwt library
        # TODO: Update the Login activity

        user_obj.last_login = timezone.now()
        return Response(
            {
                'code': 200,
                'message': 'success',
                'access_token': '',
                'refresh_token': 'refresh_token',
                'user_id': user_obj.pk,
                'name': user_obj.first_name,
                'email': user_obj.email,
                'last_login': user_obj.last_login,
            },
        )


class MeViewSet(ListViewSet):
    authentication_classes = ()  # ToDO Specify Auth class
    permission_classes = ()
    serializer_class = None  # ToDO Specify serializer_class class
    queryset = get_user_model().objects.all()

    def list(self, request, *args, **kwargs):
        # ToDO:  Add your code
        return Response({})
