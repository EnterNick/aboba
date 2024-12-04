from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken


class UserObtainTokenSerializer(serializers.Serializer):
    access = serializers.CharField(read_only=True)

    refresh = serializers.CharField(read_only=True)

    user = serializers.PrimaryKeyRelatedField(read_only=True)

    def validate(self, data):
        user = get_user_model().objects.get(pk=self.initial_data['user'])
        try:
            validated_data = {
                'access_token': str(AccessToken.for_user(user)),
                'refresh_token': str(RefreshToken.for_user(user)),
            }
            return validated_data
        except KeyError:
            raise KeyError('data argument must provide user instance with key "user"')

    @property
    def data(self):
        return self.validated_data
