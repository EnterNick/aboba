from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers.requestSerializers import (
    LoginRequestSerializer,
    RegistrationRequestSerializer,
)
from .serializers.responseSerializers import UserObtainTokenSerializer
from ..utils import get_user


class UserRegistrationView(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = RegistrationRequestSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'user_auth/registration.html'

    def get(self, request, *args, **kwargs):
        return Response(
            template_name=self.template_name, data={'user_instance': get_user(request)}
        )

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code not in [200, 201]:
            return response
        return redirect('login')


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
        return Response(
            template_name=self.template_name, data={'user_instance': get_user(request)}
        )


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        r_token = request.COOKIES.get('refreshToken')

        token = RefreshToken(r_token)
        token.blacklist()

        response = redirect('login')

        response.delete_cookie('accessToken')
        response.delete_cookie('refreshToken')

        return response
