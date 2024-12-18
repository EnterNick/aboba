from apps.feedback.models import FeedbackTicket
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.renderers import TemplateHTMLRenderer

from ..feedback.serializers.modelSerializers import FeedbackSerializer
from ..utils import get_user


class FeedbackView(CreateAPIView):
    serializer_class = FeedbackSerializer
    queryset = FeedbackTicket.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'feedback/feedback.html'

    def get(self, request, *args, **kwargs):
        return Response(data={'user_instance': get_user(request)}, template_name=self.template_name)

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        return redirect('main')
