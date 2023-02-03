from django.shortcuts import render
from Myapp1.models import Person

def MainPage(request):
    

    users_info = Person.objects.all()
    
    
    return render(request, 'MainPage.html', locals())

def GetPerson(request):
    if 
        first_name1 = request.POST.get("first_name")
        last_name1 = request.POST.get("last_name")
        salary1 = request.POST.get("salary")
        company1 = request.POST.get("company",)

        users_create = Person.objects.create(first_name = first_name1, last_name = last_name1, salary = salary1, company = company1)
    return render(request, 'creater.html', locals())
