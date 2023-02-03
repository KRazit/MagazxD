from django.contrib import admin
from django.urls import path
from Myapp1.views import MainPage, GetPerson

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPage),
    path('getter/', GetPerson),
]
