import json

from django.http import JsonResponse, HttpResponse

from artist.models import Artist

__all__ = (
    'artist_list',
)


def artist_list(request):
    artists = Artist.objects.all()

    # data = {
    #     'artists': [
    #         {
    #             'melon_id': artist.melon_id,
    #             'name': artist.name,
    #             'img_profile': artist.img_profile.url if artist.img_profile else None,
    #         }
    #         for artist in artists],
    # }

    # data = {
    #     'artists': [artist.to_json() for artist in artists],
    # }

    # data = {
    #     'artists': list(artists.values()),
    # }

    data = {
        'artists': [artist.to_json() for artist in artists],
    }

    # return HttpResponse(json.dumps(data), content_type='application/json')
    return JsonResponse(data)
