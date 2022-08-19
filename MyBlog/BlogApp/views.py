from django.contrib.auth.models import User
from .models import UserBlog
from django.shortcuts import render,redirect
from .forms import CreateUserForm
# Create your views here.

def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    form = CreateUserForm()
    return render(request,'auth/register.html',{'form':form})

def login(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
    
    return render(request,'auth/login.html')