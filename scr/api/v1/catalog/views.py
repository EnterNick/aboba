from datetime import datetime, timedelta

from apps.catalog.models import Good, Order, Category
from django.shortcuts import redirect
from django_filters import FilterSet, RangeFilter, ChoiceFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from .serializers.modelSerializer import GoodSerializer
from .serializers.requestSerializer import (
    CreateUpdateGoodSerializer,
    CreateUpdateOrderSerializer,
    FilterSerializer,
)
from ..utils import get_user
from ...auth.permissions import IsStaff, IsOwner, IsNotOwner


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

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'catalog/catalog.html'
    filter_serializer_class = FilterSerializer

    def get(self, request, *args, **kwargs):
        filter_serializer = self.filter_serializer_class(data=request.GET)
        if not filter_serializer.is_valid():
            pass
        return Response(
            data={
                'data': super().get(self, request, *args, **kwargs).data,
                'filter': filter_serializer,
                'filter_data': filter_serializer.data,
                'user': get_user(request),
            },
            template_name=self.template_name,
        )


class CreateGoodView(CreateAPIView):
    queryset = Good.objects.all()
    serializer_class = CreateUpdateGoodSerializer
    permission_classes = [IsStaff]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'catalog/create-good.html'

    def get(self, request, *args, **kwargs):
        self.check_object_permissions(request, self.request.user)
        return Response(
            data={'categories': Category.objects.values_list('title', flat=True)},
            template_name=self.template_name,
        )

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        response.data['user'] = get_user(request)
        if response.status_code == 200:
            return redirect('all_goods')
        return response


class SingleGoodEditView(RetrieveUpdateDestroyAPIView):
    queryset = Good.objects.all()
    serializer_class = CreateUpdateGoodSerializer
    permission_classes = [IsOwner]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'catalog/edit-good.html'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        response.data['categories'] = Category.objects.values_list('title', flat=True)
        return response

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('method') == 'PUT':
            self.put(request, *args, **kwargs)
            return self.get(request, *args, **kwargs)
        elif self.request.POST.get('method') == 'DELETE':
            self.delete(request, *args, **kwargs)
            return redirect('all_goods')
        else:
            return Response(data={'message': 'method not allowed'}, status=405)


class SingleGoodView(RetrieveAPIView):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
    permission_classes = [IsAuthenticated, IsNotOwner]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'catalog/good-detail.html'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        response.data['user'] = get_user(request)

        if response.status_code != 200:
            return response

        instance = self.get_object()
        if instance.owner != request.user:
            instance.has_seen += 1
            instance.save()

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
        try:
            order = Order.objects.get(good=good, user=request.user)
            order.value += int(request.POST['value'])
            order.save()
            if not order.value:
                order.delete()
            elif order.value > good.value:
                order.value = good.value
                order.save()
        except Exception:
            super().post(request, *args, **kwargs)
        return redirect('user_cart', permanent=True)


class MainPage(ListAPIView):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'catalog/catalog.html'

    def get(self, request, *args, **kwargs):
        response = super().get(self, request, *args, **kwargs)
        response.data['data'] = {'results': response.data['results']}
        response.data['user'] = get_user(request)
        return response

    def get_queryset(self):
        return self.queryset.filter(
            date_created__range=(
                datetime.today() - timedelta(weeks=1),
                datetime.today(),
            )
        ).order_by('-orders')
