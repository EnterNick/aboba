from rest_framework import serializers

from apps.catalog.models import Good, Order


class CreateUpdateGoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        exclude = [
            'id',
            'date_created',
            'cart',
            'orders',
            'have_bought',
            'has_seen',
            'income'
        ]
        read_only_fields = [
            'owner',
        ]

    def save(self, **kwargs):
        return super().save(**kwargs, owner=self.context['request'].user)


class CreateUpdateOrderSerializer(serializers.ModelSerializer):
    value = serializers.IntegerField(initial=1)

    class Meta:
        model = Order
        exclude = [
            'id',
        ]
        read_only_fields = [
            'user',
            'good',
        ]

    def save(self, **kwargs):
        request = self.context['request']
        pk = request.parser_context['kwargs']['pk']
        return super().save(**kwargs, user=self.context['request'].user, good_id=pk)

    def get_fields(self):
        fields = super().get_fields()
        request = self.context['request']
        pk = request.parser_context['kwargs']['pk']
        fields['value'] = serializers.IntegerField(
            max_value=Good.objects.get(pk=pk).value,
            initial=1,
            min_value=1,
        )
        return fields
