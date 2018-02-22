from django.shortcuts import render
from ...models import Song

__all__ = (
    'song_list',
)


def song_list(request):
    context = {
        'song_list': Song.objects.all()
    }
    return render(request, 'song/song_list.html', context)

