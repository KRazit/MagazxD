from django.shortcuts import render
from .Serializers import PersonSerializer
from .models import Person
from django.http import HttpResponse
from rest_framework import generics



class PersonAPIview(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

def MainPage(request):
    

    users_info = Person.objects.all()
    
    
    return render(request, 'MainPage.html', locals())

def UserCreate(request):
    return render(request, 'creater.html')

def SetUser(request):
    first_name_set = request.POST.get("first_name")
    last_name_set = request.POST.get("last_name")
    salary_set = request.POST.get("salary")
    company_set = request.POST.get("comapny", "Selfmade")
    set_user = Person.objects.create(first_name = first_name_set, last_name = last_name_set, salary = salary_set, company = company_set)
    return HttpResponse(f"""<a href="http://127.0.0.1:8000/"><h2>Succec</h2></a>""")
