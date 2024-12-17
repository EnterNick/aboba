from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.catalog.models import Good

from scr.api.auth.permissions import IsStaff, IsOwner
from scr.api.v1.admin.serializers.modelSerializers import GoodAdminSerializer


class AdminGoodsView(ListAPIView):
    permission_classes = [IsStaff]
    queryset = Good.objects.all()
    serializer_class = GoodAdminSerializer

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)


class AdminSingleGoodView(RetrieveAPIView):
    permission_classes = [IsOwner]
    queryset = Good.objects.all()
    serializer_class = GoodAdminSerializer
