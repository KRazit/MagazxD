from django.contrib import admin
from django.urls import path, re_path
from Myapp1.views import MainPage, UserCreate, SetUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPage),
    path('usercreate/', UserCreate),
    re_path(r'usercreate/setuser.', SetUser)
    
]
