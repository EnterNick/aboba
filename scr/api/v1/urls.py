from django.urls import path, include

from .userauth.views import UsersView, UserRegistrationView, LoginView, UserProfileView, UserCartView
from .catalog.views import GoodsView, SingleGoodView, CreateGoodView, AddToCartView

user_urlpatterns = [
    path('', UsersView.as_view(), name='all_users'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/cart/', UserCartView.as_view(), name='user_cart'),
]

goods_urlpatterns = [
    path('', GoodsView.as_view(), name='all_goods'),
    path('add/', CreateGoodView.as_view(), name='add_good'),
    path('<int:pk>/', SingleGoodView.as_view(), name='good'),
    path('<int:pk>/add-to-cart/', AddToCartView.as_view(), name='add_to_cart'),
]

urlpatterns = [
    path('users/', include(user_urlpatterns)),
    path('catalog/', include(goods_urlpatterns)),
]
