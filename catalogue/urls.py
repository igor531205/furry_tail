from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from catalogue.views import CatalogueListView

app_name = 'catalogue'

urlpatterns = [
    path('', CatalogueListView.as_view(), name='index'),

]