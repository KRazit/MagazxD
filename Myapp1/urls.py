from django.contrib import admin
from django.urls import include, path, re_path
from Myapp1.views import *
from rest_framework import routers

urlpatterns = [
    path('', MainPage),
    path('usercreate/', UserCreate),
    path('persons/<int:personsid>/', PersonPage),
    re_path(r'usercreate/setuser.', SetUser),
    path('authframework/', include('rest_framework.urls')),
    path('apiperson/', PersonAPIList.as_view()),
    path('apiperson/<int:pk>', PersonAPIUpdate.as_view()),
    path('apiperson/destroy/<int:pk>', PersonAPIDestroy.as_view()),
    path('apiperson/authdjoser/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]