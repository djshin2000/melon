import datetime

from django.shortcuts import render, redirect
from .models import Artist


def artist_list(request):
    artists = Artist.objects.all()
    context = {
        'artists': artists
    }
    return render(request, 'artist/artist_list.html', context)


def artist_add(request):
    context = {}
    if request.method == 'POST':
        name = request.POST['name']
        real_name = request.POST['real_name']
        nationality = request.POST['nationality']
        year = request.POST['year']
        month = request.POST['month']
        day = request.POST['day']
        constellation = request.POST['constellation']
        blood_type = request.POST['blood_type']
        intro = request.POST['intro']

        birth_date = year + '-' + month + '-' + day
        birth_date = datetime.datetime.strptime(birth_date, '%Y-%m-%d')

        Artist.objects.create(
            name=name,
            real_name=real_name,
            nationality=nationality,
            birth_date=birth_date,
            constellation=constellation,
            blood_type=blood_type,
            intro=intro,
        )
        return redirect('artist:artist-list')

    return render(request, 'artist/artist_add.html', context)