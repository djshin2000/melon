from django.contrib.auth import authenticate

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.exceptions import APIException, AuthenticationFailed
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class AuthTokenView(APIView):
    def post(self, request):
        # /api/members/auth-token/
        # username, password를 받음
        # 유저 인증에 성공했을 경우 토큰을 생성하거나 있으면 존재하는걸 가져와서
        # Response로 돌려줌
        # AuthTokenSerializer를 사용해서 아래 로직을 실행
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, is_create = Token.objects.get_or_create(user=user)
        # print('token >>>eastshin>>>', token.key)
        data = {
            'token': token.key,
        }
        return Response(data)

        # username = request.data.get('username')
        # password = request.data.get('password')
        # user = authenticate(request, username=username, password=password)
        # if user is not None:
        #     token, is_create = Token.objects.get_or_create(user=user)
        #     print('token >>>eastshin>>>', token.key)
        #     data = {
        #         'token': token.key,
        #     }
        #     return Response(data)
        # # authenticate에 실패했을 때
        # # raise APIException('authenticate failure~~') <- custom
        # raise AuthenticationFailed()
