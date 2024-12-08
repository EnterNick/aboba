from django.shortcuts import redirect
from django_filters import FilterSet, RangeFilter, CharFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework import filters


from apps.catalog.models import Good, Order

from .serializers.modelSerializer import GoodSerializer
from .serializers.requestSerializer import CreateUpdateGoodSerializer, CreateUpdateOrderSerializer
from .permissions import *

class PriceFilter(FilterSet):
    category = CharFilter()
    price = RangeFilter()

    class Meta:
        model = Good
        fields = ['price', 'category']


class GoodsView(ListAPIView):
    queryset = Good.objects.order_by('-orders')
    serializer_class = GoodSerializer
    filterset_class = PriceFilter
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['title', 'price', 'date_created']
    permission_classes = [IsAuthenticated]


class CreateGoodView(CreateAPIView):
    queryset = Good.objects.all()
    serializer_class = CreateUpdateGoodSerializer
    permission_classes = [IsStaff]


class SingleGoodEditView(RetrieveUpdateDestroyAPIView):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
    permission_classes = [IsOwner]


class SingleGoodView(RetrieveAPIView):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
    permission_classes = [IsAuthenticated]


class AddToCartView(CreateAPIView):
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CreateUpdateOrderSerializer

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        order = self.get_object()
        order.good.orders += 1
        order.good.save()
        return redirect('user_cart')
