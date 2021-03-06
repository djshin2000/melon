from django.shortcuts import redirect
from ...models import Song

__all__ = (
    'song_like_toggle',
)


def song_like_toggle(request, song_pk):
    song = Song.objects.get(pk=song_pk)
    if request.method == 'POST':
        song.toggle_like_user(user=request.user)
        return redirect('song:song-list')
