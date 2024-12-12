from django.contrib.auth import get_user_model
from rest_framework import serializers

from ...catalog.serializers.modelSerializer import GoodValueInCartSerializer


class UserCartSerializer(serializers.ModelSerializer):
    cart = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = [
            'cart',
        ]

    def get_cart(self, user):
        return GoodValueInCartSerializer(user.cart, many=True, context=self.context).data
