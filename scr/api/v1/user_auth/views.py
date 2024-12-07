from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers.modelSerializers import UserSerializer
from .serializers.requestSerializers import LoginRequestSerializer, RegistrationRequestSerializer
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

    def post(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(data=serializer.errors, status=422)

        token_serializer = self.token_generate_serializer(data=serializer.data)

        token_serializer.is_valid(raise_exception=True)

        return Response(data=token_serializer.data, status=200)
