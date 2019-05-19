from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^push$', views.push, name='push'),
    url(r'^produtor/(?P<id_produtor>\d+)$', views.produtor_view, name='produtor_view'),
    url(r'^produtor/(?P<id_produtor>\d+)/cattle$', views.produtor_cattle, name='produtor_cattle'),
    url(r'^produtor/(?P<id_produtor>\d+)/cattle/transfer2producer/(?P<id_boi>\d+)$', views.transfer2producer, name='transfer2producer'),
    url(r'^produtor/(?P<id_produtor>\d+)/cattle/transfer2frigo/(?P<id_boi>\d+)$', views.transfer2frigo, name='transfer2frigo'),
    url(r'^produtor/(?P<id_produtor>\d+)/criar$', views.produtor_criar, name='produtor_criar'),
    ]
