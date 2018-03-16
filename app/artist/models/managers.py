from datetime import datetime
from django.core.files import File
from django.db import models
from crawler.artist import ArtistData
from utils.file import download, get_buffer_ext


__all__ = (
    'ArtistManager',
)


class ArtistManager(models.Manager):
    def to_dict(self):
        result = []
        for instance in self.get_queryset():
            result.append(instance.to_json())
        return result
        # 기존 쿼리셋 -> self.get_queryset()
        # 특정 쿼리셋의 데이터 리스트를 dict의 list형태로 반환하도록 함
        # [
        #     {
        #         'pk': <artist pk>,
        #         'name': <artist name>,
        #         'melon_id': < artist melon id >,
        #         'img_profile': ...,
        #     },
        #     {
        #         'pk': <artist pk>,
        #         'name': <artist name>,
        #         'melon_id': < artist melon id >,
        #         'img_profile': ...,
        #     },
        # ]

    def update_or_create_from_melon(self, artist_id):
        from .artist import Artist
        artist = ArtistData(artist_id)
        artist.get_detail()
        name = artist.name
        url_img_cover = artist.url_img_cover
        real_name = artist.personal_information.get('본명', '')
        nationality = artist.personal_information.get('국적', '')
        birth_date_str = artist.personal_information.get('생일', '')
        constellation = artist.personal_information.get('별자리', '')
        blood_type = artist.personal_information.get('혈액형', '')

        # blood_type과 birth_date_str이 없을때 처리할것

        # 튜플의 리스트를 순회하며 blood_type을 결정
        for short, full in Artist.CHOICES_BLOOD_TYPE:
            if blood_type.strip() == full:
                blood_type = short
                break
        else:
            # break가 발생하지 않은 경우
            # (미리 정의해놓은 혈액형 타입에 없을 경우)
            # 기타 혈액형값으로 설정
            blood_type = Artist.BLOOD_TYPE_OTHER

        # artist_id가 melon_id에 해당하는 Artist가 이미 있다면
        #   해당 Artist의 내용을 update
        # 없으면 Artist를 생성

        artist, artist_created = self.update_or_create(
            melon_id=artist_id,
            defaults={
                'name': name,
                'real_name': real_name,
                'nationality': nationality,
                'birth_date': datetime.strptime(
                    birth_date_str, '%Y.%m.%d') if birth_date_str else None,
                'constellation': constellation,
                'blood_type': blood_type,
            }
        )
        temp_file = download(url_img_cover)
        file_name = '{artist_id}.{ext}'.format(
            artist_id=artist_id,
            ext=get_buffer_ext(temp_file)
        )
        if artist.img_profile:
            artist.img_profile.delete()
        artist.img_profile.save(file_name, File(temp_file))
        return artist, artist_created
