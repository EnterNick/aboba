from rest_framework import serializers

from apps.catalog.models import Good


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        exclude = ['cart', 'owner', 'have_bought', 'has_seen', 'income']
        read_only_fields = [
            'date_created',
            'orders',
        ]
