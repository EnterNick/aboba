from apps.catalog.models import Good, Order, Category
from rest_framework import serializers


class CreateUpdateGoodSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='title', queryset=Category.objects.all()
    )

    class Meta:
        model = Good
        exclude = [
            'id',
            'date_created',
            'cart',
            'orders',
            'have_bought',
            'has_seen',
            'income',
        ]
        read_only_fields = [
            'owner',
        ]

    def save(self, **kwargs):
        return super().save(
            **kwargs,
            owner=self.context['request'].user,
            category=self.validated_data['category'],
        )


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
        )
        return fields


class FilterSerializer(serializers.Serializer):
    price_min = serializers.FloatField(
        min_value=1, label='Минимальная цена: ', required=False
    )
    price_max = serializers.FloatField(label='Максимальная цена: ', required=False)
    try:
        category = serializers.ChoiceField(
            choices=Category.objects.values_list('id', 'title'),
            label='Категория: ',
            required=False,
        )
    except Exception:
        pass
    search = serializers.CharField(
        default='',
    )
