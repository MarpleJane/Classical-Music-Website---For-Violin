from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signUp/$', views.signUp, name='signUp'),
    url(r'^pageSinger/$', views.pageSinger, name='pageSinger'),
    url(r'^pageSinger/(?P<singer_name>\w+)/$', views.singerSong, name='singerSong'),
    url(r'^song/(?P<song_id>[0-9]+)/$', views.singleSong, name='singleSong'),
    url(r'^allSong/$', views.allSong, name='allSong'),
    url(r'^404/$', views.page404, name='page404'),
    ]
