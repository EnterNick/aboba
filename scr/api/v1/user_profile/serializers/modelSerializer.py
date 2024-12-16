from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.catalog.models import Good
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


class StaffUserSerializer(serializers.ModelSerializer):
    goods = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'first_name',
            'email',
            'avatar',
            'date_joined',
            'goods',
        ]

    @staticmethod
    def get_goods(user):
        return GoodSerializer(Good.objects.filter(owner=user), many=True).data
