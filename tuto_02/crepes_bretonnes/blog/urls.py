from django.urls import path, re_path, include
from . import views


app_name = "blog"
urlpatterns = [
    re_path(r'^$', views.home),
    path('article/<int:article_id>/', views.view_article),
    path('articles/<int:year>/<int:month>', views.list_articles),
    path('articles/<int:year>/', views.list_articles),
    path("date", views.date_actuelle),
    path("addition/<int:nombre1>/<int:nombre2>/", views.addition),
    path('contact/', views.contact, name='contact'),
    path('articleform/', views.article_form, name='articleform'),
    path('newmember/', views.NewMember, name='NewMember'),
    path('voir_members/', views.voir_members),
    #path("db_init", views.db_init)
    ]


