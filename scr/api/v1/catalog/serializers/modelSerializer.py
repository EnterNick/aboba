from apps.catalog.models import Good, Order
from rest_framework import serializers


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        exclude = [
            'cart',
            'have_bought',
            'has_seen',
            'income',
        ]
        read_only_fields = [
            'date_created',
            'orders',
        ]


class GoodValueInCartSerializer(serializers.ModelSerializer):
    val = serializers.SerializerMethodField()

    class Meta:
        model = Good
        exclude = [
            'cart',
            'owner',
            'have_bought',
            'has_seen',
            'income',
        ]
        read_only_fields = [
            'date_created',
            'orders',
        ]

    def get_val(self, good):
        return sum(
            Order.objects.filter(
                good=good, user=self.context['request'].user
            ).values_list('value', flat=True)
        )
