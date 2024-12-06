from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

from apps.catalog.models import Good
from .serializers.modelSerializer import GoodSerializer
from .serializers.requestSerializer import CreateUpdateGoodSerializer


class GoodsView(ListAPIView):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer


class CreateGoodView(CreateAPIView):
    queryset = Good.objects.all()
    serializer_class = CreateUpdateGoodSerializer


class SingleGoodView(RetrieveUpdateDestroyAPIView):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
