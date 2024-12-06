from django_filters import FilterSet, RangeFilter, CharFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import filters


from apps.catalog.models import Good
from rest_framework.pagination import PageNumberPagination

from .serializers.modelSerializer import GoodSerializer
from .serializers.requestSerializer import CreateUpdateGoodSerializer


class PriceFilter(FilterSet):
    category = CharFilter()
    price = RangeFilter()

    class Meta:
        model = Good
        fields = ['price', 'category']


class GoodsView(ListAPIView):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
    filterset_class = PriceFilter
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['title', 'price', 'date_created']



class CreateGoodView(CreateAPIView):
    queryset = Good.objects.all()
    serializer_class = CreateUpdateGoodSerializer


class SingleGoodView(RetrieveUpdateDestroyAPIView):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
