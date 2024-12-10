from rest_framework import serializers

from apps.catalog.models import Good


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        exclude = [
            'id',
            'cart',
            'owner',
        ]
        read_only_fields = [
            'date_created',
            'orders',
        ]
