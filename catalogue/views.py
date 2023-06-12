from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from common.views import TitleMixin
from catalogue.models import Animal, AnimalCategory, Favorites


class IndexView(TitleMixin, TemplateView):
    template_name = 'catalogue/index.html'
    title = 'Главная страница'


class CatalogueListView(TitleMixin, ListView):
    model = Animal
    template_name = 'catalogue/catalogue.html'
    title = 'Каталог'
    paginate_by = 6

    def get_queryset(self):
        queryset = super(CatalogueListView, self).get_queryset().order_by('id')
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CatalogueListView, self).get_context_data()
        context['categories'] = AnimalCategory.objects.all()
        return context


@login_required
def favorites_add(request, animal_id):
    Favorites.create_or_update(animal_id, request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def favorites_remove(request, favorites_id):
    favorite = Favorites.objects.get(animal_id=favorites_id)
    favorite.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
