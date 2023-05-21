from django.contrib.auth.decorators import login_required
from django.urls import path
from update.views import UpdateView

app_name = 'update'

urlpatterns = [
    path('', login_required(UpdateView.as_view()), name='index'),
]