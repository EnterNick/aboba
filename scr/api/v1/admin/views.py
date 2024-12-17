from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.catalog.models import Good

from scr.api.v1.admin.serializers.modelSerializers import GoodAdminSerializer


class AdminGoodsView(ListAPIView):
    queryset = Good.objects.all()
    serializer_class = GoodAdminSerializer

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)


class AdminSingleGoodView(RetrieveAPIView):
    queryset = Good.objects.all()
    serializer_class = GoodAdminSerializer
