from django.contrib.auth import get_user_model
from rest_framework import serializers

from ...catalog.serializers.modelSerializer import GoodSerializer


class UserSerializer(serializers.ModelSerializer):
    cart = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'first_name',
            'email',
            'avatar',
            'date_joined',
            'cart',
        ]

    @staticmethod
    def get_cart(user):
        return GoodSerializer(user.cart, many=True).data
