from django.shortcuts import render
from .models import Song


def song_list(request):
    context = {
        'song_list': Song.objects.all()
    }
    return render(request, 'song/song_list.html', context)


def song_search(request):

    return render(request, 'song/song_search.html')
