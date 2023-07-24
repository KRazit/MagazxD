from django.shortcuts import render
from .Serializers import PersonSerializer
from .models import Person
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.http import HttpResponse, HttpResponseNotFound
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework import generics, viewsets
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework.authtoken.models import Token
from rest_framework.pagination import PageNumberPagination

#Api
class PersonAPIListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000
class PersonAPIList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = PersonAPIListPagination
class PersonAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (IsOwnerOrReadOnly,)
class PersonAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (IsAdminOrReadOnly,)
#ApiEnd

#Site
def MainPage(request):
    users_info = Person.objects.all()
    title = "MainPage"
    return render(request, 'MainPage.html', locals())

def UserCreate(request):
    title = "UserCreate"
    return render(request, 'creater.html', locals())
    
def SetUser(request):
    first_name_set = request.POST.get("first_name")
    last_name_set = request.POST.get("last_name")
    salary_set = request.POST.get("salary")
    company_set = request.POST.get("comapny", "Selfmade")
    Person.objects.create(first_name = first_name_set, last_name = last_name_set, salary = salary_set, company = company_set)
    return HttpResponse(f"""<a href="http://127.0.0.1:8000/"><h2>Succec</h2></a>""")

def PersonPage(request, personsid):
    title = "Персональная страница"
    user_info = Person.objects.filter(id=personsid)
    idis = personsid
   # return HttpResponse(f"sssss {personsid}")
    return render(request, 'PersonsPage.html', locals())

def PageNotFound(request, exception):
    return HttpResponseNotFound('Ошибочка 404, Страница не найдена :(')     
#SiteEnd