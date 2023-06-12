from django.contrib import admin

from catalogue.models import Animal, AnimalCategory, Favorites

admin.site.register(AnimalCategory)


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'sex', 'age', 'price', 'quantity', 'category')
    fields = ('image', 'name', ('sex', 'age'), 'character', 'description', ('price', 'quantity'), 'category')
    search_fields = ('name',)
    ordering = ('-name',)


class FavoritesAdmin(admin.TabularInline):
    model = Favorites
    fields = ('animal', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
