from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    cart = serializers.SlugRelatedField('title', read_only=True, many=True)

    class Meta:
        model = get_user_model()
        fields = [
            'first_name',
            'email',
            'avatar',
            'date_joined',
            'cart',
        ]
