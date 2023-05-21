from django.urls import path
from django.contrib.auth.views import LogoutView

from users.views import UserLoginView, UserRegistrationView, EmailVerificationView, UserFavoritesView

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('verify/<str:username>/<uuid:code>/', EmailVerificationView.as_view(), name='email_verification'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('favorites/', UserFavoritesView.as_view(), name='favorites'),
]
