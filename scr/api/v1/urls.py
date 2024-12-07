from django.urls import path, include

from .user_auth.views import UsersView, UserRegistrationView, LoginView
from .catalog.views import GoodsView, SingleGoodView, CreateGoodView, AddToCartView
from .user_profile.views import UserProfileView, UserCartView, UserUpdateView

user_urlpatterns = [
    path('', UsersView.as_view(), name='all_users'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
]

profile_urlpatterns = [
    path('', UserProfileView.as_view(), name='profile'),
    path('cart/', UserCartView.as_view(), name='user_cart'),
    path('update/', UserUpdateView.as_view(), name='profile_update'),
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
    path('profile/', include(profile_urlpatterns)),
]
