from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers.modelSerializers import UserSerializer
from .serializers.requestSerializers import (
    LoginRequestSerializer,
    RegistrationRequestSerializer,
)
from .serializers.responseSerializers import UserObtainTokenSerializer


class UsersView(ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserRegistrationView(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = RegistrationRequestSerializer


class LoginView(APIView):
    serializer_class = LoginRequestSerializer
    token_generate_serializer = UserObtainTokenSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'user_auth/login.html'

    def post(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=422)

        token_serializer = self.token_generate_serializer(data=serializer.data)

        token_serializer.is_valid(raise_exception=True)

        response = redirect('all_goods')

        response.set_cookie('accessToken', token_serializer.data['access_token'])
        response.set_cookie('refreshToken', token_serializer.data['refresh_token'])

        return response

    def get(self, request, *args, **kwargs):
        return Response(template_name=self.template_name)
