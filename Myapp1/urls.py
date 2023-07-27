from django.contrib import admin
from django.urls import include, path, re_path
from Myapp1.views import *
from rest_framework import routers

urlpatterns = [
    path('', MainPage, name='home'),
    path('usercreate/', UserCreate, name='usercreate'),
    path('persons/<int:personsid>/', PersonPage, name='persons'),
    re_path(r'usercreate/setuser.', SetUser, name='setuser'),
    path('authframework/', include('rest_framework.urls')),
    path('apiperson/', PersonAPIList.as_view(), name='getpersonsapi'),
    path('apiperson/<int:pk>', PersonAPIUpdate.as_view(), name='personpageapi'),
    path('apiperson/destroy/<int:pk>', PersonAPIDestroy.as_view(), name='deletepersonapi'),
    path('apiperson/authdjoser/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]