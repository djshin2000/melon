from django.conf import settings
from django.db import models
from .artist import Artist

__all__ = (
    'ArtistLike',
)


class ArtistLike(models.Model):
    artist = models.ForeignKey(
        Artist,
        related_name='like_user_info_list',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='like_artist_info_list',
        on_delete=models.CASCADE,
    )
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            ('artist', 'user'),
        )

    def __str__(self):
        return 'ArtistLike (User: {user}, Artist: {artist}, created: {created})'.format(
            user=self.user,
            artist=self.artist,
            created=self.created_date,
        )
