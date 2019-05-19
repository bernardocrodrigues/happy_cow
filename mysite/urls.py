
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^', include('happy_cow.urls'))]


urlpatterns += staticfiles_urlpatterns()
