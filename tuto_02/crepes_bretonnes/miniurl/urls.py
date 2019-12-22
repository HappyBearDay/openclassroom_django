from django.urls import path, re_path, include
from . import views


app_name = "miniurl"
urlpatterns = [
    path('home/', views.list_url),
    re_path(r'^$', views.list_url),
    path('redirection_url/<reduced_url>/', views.redirection_url,  name='url_redirection'),

    ]
