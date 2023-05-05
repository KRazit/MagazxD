from django.contrib import admin
from django.urls import include, path, re_path
from Myapp1.views import *
from rest_framework import routers


#router = routers.DefaultRouter()
#router.register(r'apiperson', PersonViewSet, basename="person")
#print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Myapp1.urls')),
]

handler404 = PageNotFound