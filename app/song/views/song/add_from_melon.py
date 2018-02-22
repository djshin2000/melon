from django.shortcuts import redirect

from artist.models import Artist
from crawler.song import SongData
from song.models import Song

__all__ = (
    'song_add_from_melon',
)


def song_add_from_melon(request):
    if request.method == 'POST':
        song_id = request.POST['song_id']
        song = SongData(song_id)
        song.get_detail()

        artist = Artist.objects.update_or_create_from_melon(song.artist_id)
        song, _ = Song.objects.update_or_create(
            melon_id=song_id,
            defaults={
                'title': song.title,
                'genre': song.genre,
                'lyrics': song.lyrics,
            }
        )
        song.artists.add(artist)
        return redirect('song:song-list')
