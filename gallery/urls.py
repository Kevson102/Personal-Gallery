from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$', views.home, name='home'),
    url(r'^details/(?P<photo_id>\d+)', views.image_details, name='image_details'),
    url(r'^search/', views.search_photos, name='search_photos')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
