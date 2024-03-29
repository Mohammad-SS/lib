"""Mylibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url , include
from django.contrib import admin
from Journal import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$' , views.index  , name='index'),
    url(r'^issues/(?P<vol>[0-9]+)/(?P<iss>[0-9]+)/$', views.issues , name='issues'),
    url(r'^issues/abs/(?P<pk>[0-9]+)$', views.articlesabs , name='articleabs'),
    url(r'^issues/ref/(?P<pk>[0-9]+)$', views.articlesref , name='articlerefs'),
    url(r'^issues/pdf/(?P<pk>[0-9]+)$', views.articlespdf , name='articlepdf'),
    url(r'^purchase/(?P<pk>[0-9]+)$', views.login , name='userlogin'),
    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


