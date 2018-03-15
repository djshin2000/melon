from django.http import JsonResponse

from artist.models import Artist


def artist_list(request):
    artists = Artist.objects.all()
    data = {
        'artists': artists
    }
    return JsonResponse(data)
