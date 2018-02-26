import datetime
from django.shortcuts import render, redirect

from ...forms import ArtistAddForm
from ...models import Artist

__all__ = (
    'artist_add',
)


def artist_add(request):
    context = {}
    if request.method == 'POST':
        # multipart/form-data로 전달된 파일은 request.FILES에 들어 있음
        form = ArtistAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('artist:artist-list')
    else:
        form = ArtistAddForm()
    context['artist_add_form'] = form
    return render(request, 'artist/artist_add.html', context)
