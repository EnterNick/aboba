from rest_framework import serializers

from apps.catalog.models import Good


class CreateUpdateGoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        exclude = ['id', 'date_created',]
