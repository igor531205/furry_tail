from django.conf import settings
from django.db import models

from users.models import User


class AnimalCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=256)
    sex = models.CharField(max_length=32, null=True, blank=True)
    age = models.PositiveSmallIntegerField(default=0)
    character = models.CharField(max_length=64, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='animals_images', null=True, blank=True)
    category = models.ForeignKey(to=AnimalCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'animal'
        verbose_name_plural = 'animals'

    def __str__(self):
        return f'{self.name} | {self.category.name}'


class Favorites(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    animal = models.ForeignKey(to=Animal, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} | {self.animal.name}'

    @classmethod
    def create_or_update(cls, animal_id, user):
        favorites = Favorites.objects.filter(user=user, animal_id=animal_id)

        if not favorites.exists():
            obj = Favorites.objects.create(user=user, animal_id=animal_id, quantity=1)
            is_created = True
            return obj, is_created
        else:
            favorite = favorites.first()
            favorite.quantity += 1
            favorite.save()
            is_created = False
            return favorite, is_created
