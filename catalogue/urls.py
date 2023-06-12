from django.urls import path

from catalogue.views import CatalogueListView, favorites_add, favorites_remove
#,\
#                            shelter_add, shelter_remove

app_name = 'catalogue'

urlpatterns = [
    path('', CatalogueListView.as_view(), name='index'),
    path('category/<int:category_id>/', CatalogueListView.as_view(), name='category'),
    path('page/<int:page>/', CatalogueListView.as_view(), name='paginator'),

    path('favorites/add/<int:animal_id>/', favorites_add, name='favorites_add'),
    path('favorites/remove/<int:favorites_id>/', favorites_remove, name='favorites_remove'),

#    path('shelter/add/<int:animal_id>/', shelter_add, name='shelter_add'),
#    path('shelter/remove/<int:shelter_id>/', shelter_remove, name='shelter_remove'),
]
