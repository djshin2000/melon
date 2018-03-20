from django.urls import path
from .. import apis

app_name = 'artist'
urlpatterns = [
    # path('', apis.artist_list, name='artist-list'),
    path('', apis.ArtistList.as_view(), name='artist-drf-list'),
    path('<int:pk>/', apis.ArtistDetail.as_view(), name='artist-drf-detail'),
]
