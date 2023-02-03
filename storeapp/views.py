from django.shortcuts import render
from .models import Principal,Teacher,Facility
# Create your views here.
def homeview(request):
    facility = Facility.objects.all()
    context={'facility': facility}
    return render(request,'storeapp/home.html',context)

def aboutview(request):
    principal = Principal.objects.all()
    teacher = Teacher.objects.all()
    context={'principal': principal,'teacher':teacher}
    return render(request,'storeapp/about.html',context) 


def course(request):
    return render(request,'storeapp/course.html')

def cotact(request):
    return render(request,'storeapp/contract.html')

def loginpage(request):
    return render(request,'storeapp/login.html')

def registerpage(request):
    return render(request,'storeapp/register.html')    