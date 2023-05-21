from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.utils.timezone import now
from django.urls import reverse
from django.conf import settings


class User(AbstractUser):
    image = models.ImageField(
        upload_to='users/img', null=True, blank=True)
    is_verified_email = models.BooleanField(default=False)


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return f'EmailVerification object for {self.user.username}'

    def send_verification_email(self):
        link = reverse('users:email_verification',
                       kwargs={'username': self.user.username, 'code': self.code})
        verification_link = f'https://{settings.DOMAIN_NAME}{link}'
        subject = f'Подтверждение учетной записи для {self.user.username}'
        message = f'{self.user.username}, для подтверждения учетной записи ' +\
            f'{self.user.email} перейдите по ссылке: {verification_link}'
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False,
        )

    def is_expired(self):
        return True if now() >= self.expiration else False
