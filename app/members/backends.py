import requests
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files import File
from rest_framework import status

from utils.file import download, get_buffer_ext

User = get_user_model()


class APIFacebookBackend:
    CLIENT_ID = settings.FACEBOOK_APP_ID
    CLIENT_SECRET = settings.FACEBOOK_SECRET_CODE

    def authenticate(self, request, access_token):
        # 다 작성하고 settings.py의 AUTHENTICATION_BACKEND에 항목 추가
        params = {
            'access_token': access_token,
            'fields': ','.join([
                'id',
                'name',
                'picture.width(2500)',
                'first_name',
                'last_name',
            ])
        }
        response = requests.get('https://graph.facebook.com/v2.12/me', params)
        if response.status_code == status.HTTP_200_OK:
            response_dict = response.json()
            facebook_id = response_dict['id']
            user, _ = User.objects.get_or_create(username=facebook_id)
            return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


class FacebookBackend:
    CLIENT_ID = settings.FACEBOOK_APP_ID
    CLIENT_SECRET = settings.FACEBOOK_SECRET_CODE
    URL_ACCESS_TOKEN = 'https://graph.facebook.com/v2.12/oauth/access_token'
    URL_ME = 'https://graph.facebook.com/v2.12/me'

    def authenticate(self, request, code):
        def get_access_token(auth_code):
            params_access_token = {
                'client_id': self.CLIENT_ID,
                'redirect_uri': 'http://localhost:8000/facebook-login/',
                'client_secret': self.CLIENT_SECRET,
                'code': auth_code,
            }
            response = requests.get(self.URL_ACCESS_TOKEN, params_access_token)
            response_dict = response.json()
            return response_dict['access_token']

        def get_user_info(user_access_token):

            params = {
                'access_token': user_access_token,
                'fields': ','.join([
                    'id',
                    'name',
                    'picture.width(2500)',
                    'first_name',
                    'last_name',
                ])
            }
            response = requests.get(self.URL_ME, params)
            response_dict = response.json()
            return response_dict

        try:
            access_token = get_access_token(code)
            user_info = get_user_info(access_token)

            facebook_id = user_info['id']
            name = user_info['name']
            first_name = user_info['first_name']
            last_name = user_info['last_name']
            url_picture = user_info['picture']['data']['url']

            try:
                user = User.objects.get(username=facebook_id)
            except User.DoseNotExist:
                user = User.objects.create_user(
                    username=facebook_id,
                    first_name=first_name,
                    last_name=last_name,
                )
            if not user.img_profile:
                temp_file = download(url_picture)
                ext = get_buffer_ext(temp_file)
                user.img_profile.save(f'{user.pk}.{ext}', File(temp_file))
            return user
        except Exception:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
