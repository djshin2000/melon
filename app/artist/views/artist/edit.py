from django.shortcuts import redirect, render, get_object_or_404

from ...models import Artist
from ...forms import ArtistAddForm

__all__ = (
    'artist_edit',
)


def artist_edit(request, artist_pk):
    context = {}
    artist = get_object_or_404(Artist, pk=artist_pk)
    if request.method == 'POST':
        form = ArtistAddForm(request.POST, request.FIELS, instance=artist)
        if form.is_valid():
            form.save()
            return redirect('artist:artist-list')
    else:
        form = ArtistAddForm(instance=artist)
        context['artist_form'] = form
        return render(request, 'artist/artist_edit.html', context)
