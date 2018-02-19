from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from .models import Song


def song_list(request):
    context = {
        'song_list': Song.objects.all()
    }
    return render(request, 'song/song_list.html', context)


def song_search(request):
    # song과 연결된 Artist의 name에 keyword가 포함되는 경우
    # song과 연결된 Album의 title에 keyword가 포함되는 경우
    # song의 title에 keyword가 포함되는 경우
    #   를 모두 포함(or -> Q object)하는 쿼리셋츨 'songs'에 할당

    # songs_from_artists
    # songs_from_albums
    # songs_from_title
    #   위 세 변수에 더 위의 조건 3개에 부합하는 쿼리셋을 각각 전달
    #   세 변수를 이용해 검색 결과를 3단으로 분리해서 출력
    #   -> 아티스트로 검색한 노래 결과, 앨범으로 검색한 노래 결과, 제목으로 검색한 노래 결과
    context = {}
    if request.method == 'POST':
        keyword = request.POST['keyword'].strip()
        if keyword:
            # songs = Song.objects.filter(
            #     Q(album__title__contains=keyword) |
            #     Q(album__artists__name__contains=keyword) |
            #     Q(title__contains=keyword)
            # ).distinct()
            songs_from_title = Song.objects.filter(title__contains=keyword)
            songs_from_albums = Song.objects.filter(album__title__contains=keyword)
            songs_from_artists = Song.objects.filter(album__artists__name__contains=keyword)
            context['songs_from_title'] = songs_from_title
            context['songs_from_albums'] = songs_from_albums
            context['songs_from_artists'] = songs_from_artists
            context['keyword'] = keyword
    return render(request, 'song/song_search.html', context)
