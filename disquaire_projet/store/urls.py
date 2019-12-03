
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    re_path(r'^$', views.listing),
    re_path(r'^(?P<album_id>[0-9]+)/$', views.detail),
    re_path(r'^search/$', views.search),
    ]