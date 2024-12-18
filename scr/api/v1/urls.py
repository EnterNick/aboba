from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.urls import path, include, re_path

from .admin.views import AdminGoodsView, AdminSingleGoodView
from .catalog.views import (
    GoodsView,
    SingleGoodView,
    CreateGoodView,
    AddToCartView,
    SingleGoodEditView,
    MainPage,
)
from .feedback.views import FeedbackView
from .user_auth.views import UserRegistrationView, LoginView, LogoutView
from .user_profile.views import UserProfileView, UserCartView, UserUpdateView
from .support_chat.consumers import ChatConsumer
from .support_chat.views import ChatView

user_urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
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
    path('edit/', UserUpdateView.as_view(), name='profile_update'),
]

goods_urlpatterns = [
    path('', GoodsView.as_view(), name='all_goods'),
    path('add/', CreateGoodView.as_view(), name='add_good'),
    path('<int:pk>/', SingleGoodView.as_view(), name='good'),
    path('<int:pk>/edit/', SingleGoodEditView.as_view(), name='edit_good'),
    path('<int:pk>/add-to-cart/', AddToCartView.as_view(), name='add_to_cart'),
]

admin_urlpatterns = [
    path('', AdminGoodsView.as_view(), name='admin_goods'),
    path('<int:pk>/', AdminSingleGoodView.as_view(), name='admin_goods-detail'),
]

feedback_urlpatterns = [path('', FeedbackView.as_view(), name='feedback')]

websocket_urlpatterns = [
    re_path(r'ws/msg/(?P<pk>\d+)/$', ChatConsumer.as_asgi()),
]

support_chat_urlpatterns = [path('<int:pk>/', ChatView.as_view(), name='chat')]

urlpatterns = [
    path('users/', include(user_urlpatterns)),
    path('catalog/', include(goods_urlpatterns)),
    path('profile/', include(profile_urlpatterns)),
    path('analytics/', include(admin_urlpatterns)),
    path('feedback/', include(feedback_urlpatterns)),
    path('chat/', include(support_chat_urlpatterns)),
    path('main/', MainPage.as_view(), name='main'),
]
