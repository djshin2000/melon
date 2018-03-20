from django.http import JsonResponse, HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from utils.pagination import SmallPagination
from ...models import Artist
from ...serializers import ArtistSerializer

__all__ = (
    'ArtistList',
    'ArtistDetail',
)


# class ArtistListView(APIView):
#     # generics의 요소를 사용해서
#     # ArtistListCreateView, ArtistRetrieveUpdateDestroyView
#     #   2개를 구현 / URL과 연결 / Postman에 API테스트 구현
#     def get(self, request):
#         artists = Artist.objects.all()
#         serializer = ArtistSerializer(artists, many=True)
#         return Response(serializer.data)


class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    pagination_class = SmallPagination

    # def get(self, request, *args, **kwargs):
    #     print('request.user:', request.user)
    #     return super().get(request, *args, **kwargs)

    # def perform_create(self, serializer):
    #     serializer.save()


class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

# 1. 특정 유저의 Token 을 생성
# 2. TokenAuthentication을 사용하도록 REST_FRAMEWORK설정
# 3. Postman의 HTTP Header 'Authorization'에
#       Token <value> <- 지정
# 4. 요청 후 request.user가 정상적으로 출력되는지 확인
