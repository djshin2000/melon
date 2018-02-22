from typing import NamedTuple
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

    context = {
        'song_infos': [],
    }
    keyword = request.GET.get('keyword') # dic에 keyword를 가져오고 없으면 null

    class SongInfo(NamedTuple):
        type: str
        q: Q

    if keyword:
        song_infos = (
            SongInfo(
                type='아티스트명',
                q=Q(album__artists__name__contains=keyword)),
            SongInfo(
                type='앨범명',
                q=Q(album__title__contains=keyword)),
            SongInfo(
                type='노래제목',
                q=Q(title__contains=keyword)),
        )
        for type, q in song_infos:
            context['song_infos'].append({
                'type': type,
                'songs': Song.objects.filter(q),
            })
    return render(request, 'song/song_search.html', context)


def song_add_from_melon(request):
    # 패키지 분할 (artist랑 똑같은 형태로)
    # artist_add_from_melon과 같은 기능을 함
    # song_search_from_melon도 구현
    # -> 이 안에 'DB에 추가'하는 Form구현
    pass
