from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.urls import path, include

from .catalog.views import (
    GoodsView,
    SingleGoodView,
    CreateGoodView,
    AddToCartView,
    SingleGoodEditView,
)
from .user_auth.views import UsersView, UserRegistrationView, LoginView
from .user_profile.views import UserProfileView, UserCartView, UserUpdateView

user_urlpatterns = [
    path('', UsersView.as_view(), name='all_users'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('reset_password/', PasswordResetView.as_view(), name='reset_password'),
    path(
        'reset_password_sent/',
        PasswordResetDoneView.as_view(),
        name='password_reset_done',
    ),
    path(
        'reset/<int:pk>/<token>',
        PasswordResetConfirmView.as_view(),
        name='password_reset_confirm',
    ),
    path(
        'reset_password_complete/',
        PasswordResetCompleteView.as_view(),
        name='password_reset_complete',
    ),
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
    path('<int:pk>/edit/', SingleGoodEditView.as_view(), name='edit_good'),
    path('<int:pk>/add-to-cart/', AddToCartView.as_view(), name='add_to_cart'),
]

urlpatterns = [
    path('users/', include(user_urlpatterns)),
    path('catalog/', include(goods_urlpatterns)),
    path('profile/', include(profile_urlpatterns)),
]
