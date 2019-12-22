"""crepes_bretonnes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,re_path, include
from blog import views as blog_views
from miniurl import views as miniurl_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),#Don't forget to rename this path
    re_path(r'^$', blog_views.home),
    path('acceuil', blog_views.home),
    path('home', blog_views.home),
    path('about/', blog_views.about),
    path('add_url/', miniurl_views.NewUrl),
    path('blog/', include('blog.urls', namespace = "blog")),
    path('miniurl/', include('miniurl.urls', namespace = "miniurl")),
]

urlpatterns += static(
    settings.MEDIA_URL, 
    document_root=settings.MEDIA_ROOT)