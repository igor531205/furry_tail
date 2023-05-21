from os import system

from django.views.generic.base import RedirectView


class UpdateView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'index'

    def get_redirect_url(self, *args, **kwargs):
        system('git -C ~/furry_tail/ pull origin main')
        return super().get_redirect_url(*args, **kwargs)
