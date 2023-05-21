from os import system

from django.views.generic.base import RedirectView


class UpdateView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'index'

    def get_redirect_url(self, *args, **kwargs):
        system('git -C ~/furry_tail/ pull origin main')
        system('sudo systemctl restart nginx')
        system('sudo systemctl restart gunicorn')
        system('sudo systemctl restart celery')
        return super().get_redirect_url(*args, **kwargs)
