from django.views.generic.base import TemplateView

from common.views import TitleMixin


class IndexView(TitleMixin, TemplateView):
    template_name = 'catalogue/index.html'
    title = 'Главная страница'


class CatalogueListView(TitleMixin, TemplateView):
    template_name = 'catalogue/catalogue.html'
    title = 'Каталог'
