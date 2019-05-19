from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^push$', views.push, name='push'),
    url(r'^produtor/(?P<id_produtor>\d+)$', views.produtor_view, name='produtor_view'),
    url(r'^produtor/criar$', views.produtor_criar, name='produtor_criar'),
    ]
