from django.contrib.auth import get_user_model
from rest_framework import serializers

from ...catalog.serializers.modelSerializer import GoodSerializer


class UserCartSerializer(serializers.ModelSerializer):
    cart = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = [
            'cart',
        ]

    def get_cart(self, user):
        return GoodSerializer(user.cart, many=True).data
