from django.urls import path

from .userauth.views import UsersView, UserRegistrationView, LoginView, UserProfileView

urlpatterns = [
    path('', UsersView.as_view(), name='all_users'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]
