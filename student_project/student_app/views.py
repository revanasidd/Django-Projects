from django.shortcuts import render
from django.http import HttpResponse
from .forms import student_form
from .models import Student

# Create your views here.

def index(request):
    return HttpResponse("this is my first webpage without html file on server")

def index2(request):
    return HttpResponse("this is my second page")

def index3(request):
    return HttpResponse("<a href='path4'> this is my third page</a>")

def index4(request):
    return HttpResponse("this is my ")

def index5(request):
    return HttpResponse("this is my first webpage without html file on server")

def index6(request):
    return HttpResponse("this is my first webpage without html file on server")

def index7(request):
    return HttpResponse("this is my first webpage without html file on server")

def index8(request):
    return HttpResponse("this is my first webpage without html file on server")

def index9(request):
    return HttpResponse("this is my first webpage without html file on server")

def form(request):
    return HttpResponse("<h1>first heading</h1><p>")

def htmlfile(request):
    return render(request, 'index.html')

def form(request):
    if request.method=='GET':
        data=student_form
    else:
        data=student_form(request.POST)
        if data.is_valid():
            data.save()
    return render(request, 'form.html', {'form':data})

def list(request):
    show_data=Student.objects.all()
    return render(request, 'list.html',{'list':show_data})