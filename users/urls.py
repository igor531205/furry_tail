from django.urls import path
from django.contrib.auth.views import LogoutView

from users.views import UserLoginView, UserRegistrationView

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
