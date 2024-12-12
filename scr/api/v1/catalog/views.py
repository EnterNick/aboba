from django.shortcuts import redirect
from django_filters import FilterSet, RangeFilter, ChoiceFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
)
from rest_framework import filters
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.catalog.models import Good, Order, Category

from .serializers.modelSerializer import GoodSerializer
from .serializers.requestSerializer import (
    CreateUpdateGoodSerializer,
    CreateUpdateOrderSerializer,
    FilterSerializer,
)
from ...auth.permissions import IsStaff, IsOwner


class PriceFilter(FilterSet):
    category = ChoiceFilter(
        initial='1',
        choices=Category.objects.values_list('id', 'title'),
    )
    price = RangeFilter()

    class Meta:
        model = Good
        fields = ['price', 'category']


class GoodsView(ListAPIView):
    queryset = Good.objects.order_by('-orders')
    serializer_class = GoodSerializer
    filterset_class = PriceFilter
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    search_fields = ['title', 'description']
    ordering_fields = ['title', 'price', 'date_created']
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'catalog/catalog.html'
    filter_serializer_class = FilterSerializer

    def get(self, request, *args, **kwargs):
        filter_serializer = self.filter_serializer_class(
            data={
                'price_min': request.GET.get('price_min'),
                'price_max': request.GET.get('price_max'),
                'category': request.GET.get('category', 1),
            }
        )
        if not filter_serializer.is_valid():
            filter_serializer = self.filter_serializer_class()
        return Response(
            data={
                'data': super().get(self, request, *args, **kwargs).data,
                'filter': filter_serializer,
            },
            template_name=self.template_name,
        )


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
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'catalog/good-detail.html'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        if response.status_code != 200:
            return response
        instance = self.get_object()
        if instance.owner != request.user:
            instance.has_seen += 1
            instance.save()
        response.data = {'product': response.data}
        return response


class AddToCartView(CreateAPIView):
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CreateUpdateOrderSerializer

    def post(self, request, *args, **kwargs):
        good = Good.objects.get(pk=request.parser_context['kwargs']['pk'])
        if request.user == good.owner:
            return Response(
                data={'message': 'Нельзя добавить свой товар в корзину'}, status=403
            )
        super().post(request, *args, **kwargs)
        return redirect('user_cart')
