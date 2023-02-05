from django.contrib import admin
from django.urls import path, re_path
from Myapp1.views import MainPage, PersonAPIview, UserCreate, SetUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPage),
    path('usercreate/', UserCreate),
    re_path(r'usercreate/setuser.', SetUser),
    re_path(r'apiperson.', PersonAPIview.as_view())
    
]
