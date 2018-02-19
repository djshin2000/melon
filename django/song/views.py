from django.http import HttpResponse
from django.shortcuts import render
from .models import Song


def song_list(request):
    context = {
        'song_list': Song.objects.all()
    }
    return render(request, 'song/song_list.html', context)


def song_search(request):
    context = {}
    if request.method == 'POST':
        keyword = request.POST['keyword'].strip()
        if keyword:
            songs = Song.objects.filter(title__contains=keyword)
            context['songs'] = songs
    return render(request, 'song/song_search.html', context)
