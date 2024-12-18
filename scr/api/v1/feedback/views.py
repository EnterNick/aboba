from apps.feedback.models import FeedbackTicket
from rest_framework.generics import CreateAPIView

from ..feedback.serializers.modelSerializers import FeedbackSerializer


class FeedbackView(CreateAPIView):
    serializer_class = FeedbackSerializer
    queryset = FeedbackTicket.objects.all()
