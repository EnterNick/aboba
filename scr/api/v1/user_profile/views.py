from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.catalog.models import Order
from .serializers.modelSerializer import UserSerializer
from .serializers.responseSerilaizers import UserCartSerializer


class UserProfileView(RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserCartView(RetrieveAPIView):
    serializer_class = UserCartSerializer
    queryset = get_user_model().objects.all()
    permission_classes = [IsAuthenticated]

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
