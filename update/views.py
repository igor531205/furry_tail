from os import system

from django.views.generic.base import RedirectView
from django.contrib.messages.views import SuccessMessageMixin


class UpdateView(SuccessMessageMixin, RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'index'
    success_message = 'Project Update'

    def get_redirect_url(self, *args, **kwargs):
        system('git -C ~/furry_tail/ pull origin main')
        system('sudo systemctl restart nginx')
        system('sudo systemctl restart gunicorn')
        system('sudo systemctl restart celery')
        return super().get_redirect_url(*args, **kwargs)
