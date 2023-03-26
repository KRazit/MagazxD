from django.contrib import admin
from django.urls import include, path, re_path
from Myapp1.views import *
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'apiperson', PersonViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPage),
    path('usercreate/', UserCreate),
    re_path(r'usercreate/setuser.', SetUser),
    path('', include(router.urls)),
 #   path('apiperson/', PersonViewSet.as_view({'get': 'list'})),
  #  path('apiperson/<int:pk>/', PersonViewSet.as_view({'put': 'update', 'delete': 'destroy', 'get': 'retrieve'})),
]
