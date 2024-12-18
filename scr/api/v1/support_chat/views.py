from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1.utils import get_user


class ChatView(APIView):
    template_name = 'support_chat/chat.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        return Response(
            data={'user_instance': get_user(request)}, template_name=self.template_name
        )
