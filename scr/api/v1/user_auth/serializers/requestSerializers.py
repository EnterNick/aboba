from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.serializers import ValidationError


class LoginRequestSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=100, required=True)

    password = serializers.CharField(max_length=120, write_only=True, required=True)

    user = serializers.PrimaryKeyRelatedField(read_only=True)

    def validate(self, data):
        user = get_user_model().objects.filter(email=data['email']).first()

        if user is None or not user.is_active:
            raise ValidationError('Логин неправильный!')

        if not user.check_password(data['password']):
            raise ValidationError('Пароль неправильный!')

        data['user'] = user
        return data


class RegistrationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'avatar',
            'password',
        ]
        extra_kwargs = {
            'password': {
                'write_only': True,
            },
        }

    @staticmethod
    def validate_password(password):
        validate_password(password)
        return make_password(password)
