import re
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from crawler.utils.parsing import get_dict_from_dl

__all__ = (
    'AlbumData',
)


class AlbumData:
    def __init__(self, album_id, title='', url_img_cover='', release_date=''):
        self.album_id = album_id
        self.title = title
        self.url_img_cover = url_img_cover
        self.release_date = release_date

    def __str__(self):
        return self.title

    def get_detail(self):
        url = 'https://www.melon.com/album/detail.htm'
        params = {
            'albumId': self.album_id,
        }
        response = requests.get(url, params)
        source = response.text
        soup = BeautifulSoup(source, 'lxml')
        wrap_info = soup.select_one('div.wrap_info')
        entry = wrap_info.select_one('div.entry')
        title = entry.select_one('.info > .song_name').strong.next_sibling.strip()
        meta = entry.select_one('.meta > dl.list')
        album_meta_dict = get_dict_from_dl(meta, first_text=True)
        release_date = album_meta_dict.get('발매일')
        img_url_full = wrap_info.select_one('div.thumb > a > img').get('src')
        img_url_list = re.split('\?', img_url_full)
        img_url = img_url_list[0]

        # print(title)
        # print(album_meta_dict)
        # print(img_url_full)
        # print(img_url_list[0])
        # file_name = Path(img_url).name
        # print(file_name)

        self.title = title
        self.url_img_cover = img_url
        self.release_date = release_date


AlbumData(album_id='10096855').get_detail()
