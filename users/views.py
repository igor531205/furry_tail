from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from users.models import User, EmailVerification
from common.views import TitleMixin


class UserLoginView(TitleMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Авторизация'


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    title = 'Регистрация'
    success_url = reverse_lazy('users:login')
    success_message = 'Вы успешно зарегистрированы!'


class EmailVerificationView(TitleMixin, TemplateView):
    title = 'Подтверждение электронной почты'
    template_name = 'users/email_verification.html'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verifications = EmailVerification.objects.filter(user=user, code=code)
        if email_verifications.exists() and not email_verifications.first().is_expired():
            user.is_verified_email = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('index'))
