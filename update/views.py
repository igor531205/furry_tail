from os import system

from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView, RedirectView

from common.views import TitleMixin


class UpdateView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'index'

    def get_redirect_url(self, *args, **kwargs):
        system('git -C ~/furry_tail/ pull origin main')
        return super().get_redirect_url(*args, **kwargs)
