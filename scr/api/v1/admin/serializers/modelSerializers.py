from datetime import datetime, timedelta

from apps.catalog.models import Good, VisitsPerWeek
from rest_framework import serializers


class GoodAdminSerializer(serializers.ModelSerializer):
    conversion_level = serializers.SerializerMethodField(read_only=True)
    has_seen_for_last_week = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Good

        exclude = [
            'owner',
            'date_created',
            'cart',
        ]
        read_only_fields = [
            'income',
            'has_seen',
            'have_bought',
        ]

    @staticmethod
    def get_conversion_level(obj):
        try:
            return str(round(obj.orders / obj.has_seen, 3) * 100) + '%'
        except ZeroDivisionError:
            return 0

    @staticmethod
    def get_has_seen_for_last_week(good):
        visits = VisitsPerWeek.objects.filter(good=good)
        visits_instance = visits.first()
        if not visits or visits_instance.date_crated <= (
            datetime.today() - timedelta(weeks=1)
        ):
            try:
                visits_instance.delete()
            except AttributeError:
                pass
            VisitsPerWeek.objects.create(good=good)
        if visits_instance is None:
            return 0
        return visits_instance.value
