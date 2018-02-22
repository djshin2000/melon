from django.db import models
from album.models import Album
from artist.models import Artist
from crawler.song import SongData


class SongManager(models.Manager):
    def update_or_create_from_melon_id(self, song_id):
        """
        song_id에 해당하는 Song정보를 멜론사이트에서 가져와 update_or_create를 실행
        이 때, 해당 Song의 Artist정보도 가져와 ArtistManager.update_or_create_from_melon도 실행

        그리고 해당 Song의 Album정보도 가져와서 AlbumManager.update_or_create_from_melon도 실행
            -> Album의 커버이미지도 저장해야 함

        :param song_id: 멜론 사이트에서의 곡 고유 ID
        :return: (Song instance, Bool(Song created))
        """
        song_data = SongData(song_id)
        song_data.get_detail()
        song, song_created = self.update_or_create(
            melon_id=song_id,
            defaults={
                'title': song_data.title,
                'genre': song_data.genre,
                'lyrics': song_data.lyrics,
            }
        )
        artist, _ = Artist.objects.update_or_create_from_melon(song_data.artist_id)
        song.artists.add(artist)

        album, _ = Album.objects.update_or_create_from_melon_id(song_data.album_id)
        song.album = album
        song.save()
        return song, song_created


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

    objects = SongManager()

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
