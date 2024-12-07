from rest_framework import serializers

from apps.catalog.models import Good


class CreateUpdateGoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        exclude = [
            'id',
            'date_created',
            'cart',
            'orders'
        ]
        read_only_fields = ['owner',]


    def save(self, **kwargs):
        return super().save(**kwargs, owner=self.context['request'].user)
