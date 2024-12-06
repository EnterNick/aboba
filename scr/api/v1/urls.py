from django.urls import path, include

from .userauth.views import UsersView, UserRegistrationView, LoginView, UserProfileView
from .catalog.views import GoodsView, SingleGoodView, CreateGoodView

user_urlpatterns = [
    path('', UsersView.as_view(), name='all_users'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]

goods_urlpatterns = [
    path('', GoodsView.as_view(), name='all_goods'),
    path('add/', CreateGoodView.as_view(), name='add_good'),
    path('<int:pk>/', SingleGoodView.as_view(), name='good'),
]

urlpatterns = [
    path('users/', include(user_urlpatterns)),
    path('catalog/', include(goods_urlpatterns)),
]
