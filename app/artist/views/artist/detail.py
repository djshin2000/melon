import requests
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from ...models import Artist

__all__ = (
    'artist_detail',
)


def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)

    url = 'https://www.googleapis.com/youtube/v3/search'
    params = {
        'key': settings.YOUTUBE_API_KEY,
        'part': 'snippet',
        'type': 'video',
        'maxResults': '10',
        'q': artist.name,
    }
    response = requests.get(url, params)
    response_dic = response.json()

    context = {
        'artist': artist,
        'youtube_items': response_dic['items'],
    }
    return render(request, 'artist/artist_detail.html', context)
