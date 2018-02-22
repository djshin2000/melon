from datetime import datetime
from pathlib import Path

import requests
from django.core.files import File
from django.db import models
from io import BytesIO

from crawler.album import AlbumData


class AlbumManager(models.Manager):
    def update_or_create_from_melon_id(self, album_id):
        album_data = AlbumData(album_id)
        album_data.get_detail()
        release_date_str = album_data.release_date
        url_img_cover = album_data.url_img_cover
        album, album_created = self.update_or_create(
            melon_id=album_id,
            defaults={
                'title': album_data.title,
                'release_date': datetime.strptime(
                    release_date_str, '%Y.%m.%d') if release_date_str else None,
            }
        )

        # img 파일 저장
        binary_data = requests.get(url_img_cover).content
        temp_file = BytesIO()
        temp_file.write(binary_data)
        # seek 함수가 무엇을 하는지 모르겠음
        temp_file.seek(0)
        file_name = Path(url_img_cover).name
        album.img_cover.save(file_name, File(temp_file))

        return album, album_created


class Album(models.Model):
    # 앨범명, 발매일, 장르, 발매사, 기획사, 앨범소개(intro), 평점, 앨범이미지
    melon_id = models.CharField('멜론 Album ID', max_length=20, blank=True, null=True, unique=True)
    title = models.CharField('앨범명', max_length=100)
    img_cover = models.ImageField(
        '커버 이미지',
        upload_to='album',
        blank=True,
    )
    release_date = models.DateField('발매일', blank=True, null=True)

    objects = AlbumManager()

    @property
    def genre(self):
        # 장르는 가지고 있는 노래들에서 가져오기
        return ', '.join(self.song_set.values_list('genre', flat=True).distinct())

    def __str__(self):
        # return '{title} [{artists}]'.format(
        #     title=self.title,
        #     artists=', '.join(self.artists.values_list('name', flat=True))
        # )
        return self.title
