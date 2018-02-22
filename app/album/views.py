from django.shortcuts import render
from .models import Album


def album_list(request):
    context = {
        'album_list': Album.objects.all(),
    }
    return render(request, 'album/album_list.html', context)
