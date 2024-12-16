import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.authentication import BaseAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import AccessToken


class CustomJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        try:
            access_token = request.COOKIES.get('accessToken')
            if not access_token or access_token is None:
                return None

            payload = jwt.decode(
                bytes(access_token, 'utf-8'), settings.SECRET_KEY, algorithms=['HS256']
            )

        except jwt.ExpiredSignatureError:
            refresh_token = request.COOKIES.get('refreshToken')
            if not refresh_token or refresh_token is None:
                return None
            try:
                payload = jwt.decode(
                    bytes(refresh_token, 'utf-8'),
                    settings.SECRET_KEY,
                    algorithms=['HS256'],
                )
            except jwt.ExpiredSignatureError:
                raise None

            user = get_user_model().objects.filter(id=payload.get('user_id')).first()
            if user is None:
                raise AuthenticationFailed('User not found')

            if not user.is_active:
                raise AuthenticationFailed('user is inactive')

            access_token = AccessToken.for_user(user)

            return user, access_token

        user = get_user_model().objects.filter(id=payload['user_id']).first()

        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.is_active:
            raise AuthenticationFailed('user is inactive')

        return user, access_token
