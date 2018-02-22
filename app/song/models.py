from django.db import models
from album.models import Album
from artist.models import Artist


class Song(models.Model):
    melon_id = models.CharField('멜론 Song ID', max_length=20, blank=True, null=True, unique=True)
    # 앨범(foreignkey), 제목, 가사, 장르, 작사, 작곡, 편곡, 가수(foreignkey), 좋아요,
    album = models.ForeignKey(
        Album,
        verbose_name='앨범',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    artists = models.ManyToManyField(Artist, verbose_name='아티스트 목록', blank=True)
    title = models.CharField('곡 제목', max_length=100)
    genre = models.CharField('장르', max_length=100)
    lyrics = models.TextField('가사', blank=True)

    @property
    def release_date(self):
        # self.album의 release_date를 리턴
        return self.album.release_date

    @property
    def formatted_release_date(self):
        # f2017.01.15
        return self.release_date.strftime('%Y.%m.%d')

    def __str__(self):
        # 가수명 - 곡제목(앨범명)
        # if self.album:
        #     return '{artists} - {title} ({album})'.format(
        #         artists=', '.join(self.album.artists.values_list('name', flat=True)),
        #         title=self.title,
        #         album=self.album.title,
        #     )
        return '{title} - {artist}'.format(
            title=self.title,
            artist=', '.join(self.artists.values_list('name', flat=True)),
        )
