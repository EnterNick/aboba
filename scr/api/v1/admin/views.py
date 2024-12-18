from api.auth.permissions import IsStaff, IsOwner
from api.v1.admin.serializers.modelSerializers import GoodAdminSerializer
from api.v1.utils import get_user
from apps.catalog.models import Good
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.renderers import TemplateHTMLRenderer


class AdminGoodsView(ListAPIView):
    permission_classes = [IsStaff]
    queryset = Good.objects.all()
    serializer_class = GoodAdminSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'admin/products-admin.html'

    def get(self, request, *args, **kwargs):
        response = super().get(self, request, *args, **kwargs)
        response.data['user_instance'] = get_user(request)
        return response

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)


class AdminSingleGoodView(RetrieveAPIView):
    permission_classes = [IsOwner]
    queryset = Good.objects.all()
    serializer_class = GoodAdminSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'admin/product-detail-analitycs.html'

    def get(self, request, *args, **kwargs):
        response = super().get(self, request, *args, **kwargs)
        response.data['user_instance'] = get_user(request)
        return response
