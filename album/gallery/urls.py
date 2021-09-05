from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from .views import home,get, search

urlpatterns = [
    path('',home,name="home"),
    path('load/<id>/',get,name="getUsers"),
    path('search/',search,name="search"),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
