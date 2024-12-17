from apps.catalog.models import Good, Order, VisitsPerWeek
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
    category = serializers.SlugRelatedField(slug_field='title', read_only=True)

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
        return Order.objects.get(good=good, user=self.context['request'].user).value


class MainPageGoodSerializer(serializers.ModelSerializer):
    has_seen_last_week = serializers.SerializerMethodField(read_only=True)

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

    @staticmethod
    def get_has_seen_last_week(good):
        try:
            return VisitsPerWeek.objects.get(good=good).value
        except Exception:
            return 0

    @property
    def data(self):
        _data = super().data
        _data = sorted(_data, key=lambda x: x.get('has_seen_last_week', 0))
        return _data
