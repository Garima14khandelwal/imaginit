from django.conf.urls import  include,url
from django.contrib.auth.views import logout
from main.views import (Home, ImageProcessing,
                        DeleteImage, SaveProcessedImage, Effects, Meffects, Manip, Index)


urlpatterns = [
    url(r'^$', Index, name='index'),
    url(r'^image/$', ImageProcessing.as_view(), name='image'),
    url(r'^home/', Home.as_view(), name='home'),
    url(r'^effects/', Effects.as_view(), name='effects'),
    url(r'^meffects/', Meffects.as_view(), name='meffects'),
    url(r'^manip/', Manip.as_view(), name='manip'),
    url(r'^image/(?P<id>[0-9]+)/delete/$',
        DeleteImage.as_view(), name='delete'),
    url(r'^save-effects/', SaveProcessedImage.as_view(), name='save_effects'),
   
   
]
