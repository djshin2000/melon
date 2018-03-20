from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from ..views import index
from sms.views import send_sms

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('', include('members.urls.views')),

    path('artist/', include('artist.urls.views')),
    path('song/', include('song.urls')),
    path('album/', include('album.urls')),

    path('sms/send/', send_sms, name='send-sms'),
]
# settings.MEDIA_URL('/media/')로 시작하는 요청은
# document_root인 settings.MEDIA_ROOT폴더(ROOT_DIR/.media)에서 파일을 찾아 리턴해준다
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
