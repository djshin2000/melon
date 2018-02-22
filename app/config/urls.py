"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from config import views
from members.views import login_view, logout_view

urlpatterns = [
    # path('', TemplateView.as_view(template_name='index.html')),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('artist/', include('artist.urls')),
    path('song/', include('song.urls')),
    path('album/', include('album.urls')),
]
# settings.MEDIA_URL('/media/')로 시작하는 요청은
# document_root인 settings.MEDIA_ROOT폴더(ROOT_DIR/.media)에서 파일을 찾아 리턴해준다
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)