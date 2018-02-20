from django.urls import path
from . import views

app_name = 'artist'
urlpatterns = [
    path('', views.artist_list, name='artist-list'),
    path('add/', views.artist_add, name='artist-add'),
    path('search/melon/', views.artist_search_from_melon, name='artist-search-from-melon'),
]
