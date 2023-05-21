import uuid
from datetime import timedelta

from django import forms
from django.utils.timezone import now
from django.contrib.auth.forms import \
    AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User, EmailVerification

from django.utils.translation import gettext_lazy as _

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input_text name', 'placeholder': 'Иван'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input_text password', 'placeholder': 'Введите пароль'}
    ))

    class Meta:
        model = User
        fields = ('username', 'password',)


class UserRegistrationForm(UserCreationForm):
    SEX_CHOICES = [('1', 'М'), ('2', 'Ж'), ('0', 'Не указано')]
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input_text name', 'placeholder': 'Иван'}
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input_text surname', 'placeholder': 'Иванов'}
    ))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'input_text email', 'placeholder': 'mail@mail.com'}
    ))
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input_text name', 'placeholder': 'Иван'}
    ))
    sex = forms.CharField(widget=forms.RadioSelect(
        attrs={'name': 'sex', 'class': 'sex', 'id': 'orange'}, choices=SEX_CHOICES
    ), initial=('0', 'Не указано'))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input_text password', 'placeholder': 'Введите пароль'}
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input_text password approve', 'placeholder': 'Подтвердите пароль'}
    ))


    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'sex', 'password1', 'password2',)

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=True)
        expiration = now() + timedelta(hours=48)
        record = EmailVerification.objects.create(
            code=uuid.uuid4(), user=user, expiration=expiration)
        record.send_verification_email()
        return user
