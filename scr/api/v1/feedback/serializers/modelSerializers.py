from apps.feedback.models import FeedbackTicket
from rest_framework import serializers


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackTicket
        fields = '__all__'
        read_only_fields = [
            'id',
            'user',
        ]
