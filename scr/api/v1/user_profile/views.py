from apps.catalog.models import Order
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from .serializers.modelSerializer import UserSerializer, StaffUserSerializer
from .serializers.responseSerilaizers import UserCartSerializer
from ..utils import get_user


class UserProfileView(RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'user_profile/profile.html'

    def get(self, request, *args, **kwargs):
        return Response(
            data={
                'instance': super().get(self, request, *args, **kwargs).data,
                'user': get_user(request),
            },
            template_name=self.template_name,
        )

    def get_object(self):
        return self.request.user

    def get_serializer_class(self):
        return (
            self.serializer_class
            if not self.request.user.is_staff
            else StaffUserSerializer
        )


class UserCartView(RetrieveAPIView):
    serializer_class = UserCartSerializer
    queryset = get_user_model().objects.all()
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'user_profile/cart.html'

    def get_object(self):
        return self.request.user

    def post(self, request, *args, **kwargs):
        cart = self.get_object().cart.all()
        for good in cart:
            orders = Order.objects.filter(good=good, user=self.get_object())
            for order in orders.all():
                good.income += order.value * good.price
                good.orders += 1
                good.have_bought += order.value
                good.value -= order.value
                good.save()
                order.delete()
        return redirect('all_goods')


class UserUpdateView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
