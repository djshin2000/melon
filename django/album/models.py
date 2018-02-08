from django.db import models

from artist.models import Artist


class Album(models.Model):
    # 앨범명, 발매일, 장르, 발매사, 기획사, 앨범소개(intro), 평점, 앨범이미지

    title = models.CharField('앨범명', max_length=100)
    img_cover = models.ImageField(
        '커버 이미지',
        upload_to='album',
        blank=True,
    )
    artists = models.ManyToManyField(
        Artist,
        verbose_name='아티스트 목록',
    )
    release_date = models.DateField()

    @property
    def genre(self):
        # 장르는 가지고 있는 노래들에서 가져오기
        return ''

    def __str__(self):
        return '{title} [{artists}]'.format(
            title=self.title,
            artists=', '.join(self.artists.values_list('name', flat=True))
        )
