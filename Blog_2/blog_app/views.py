from django.shortcuts import redirect, render
from .models import Blog
from django.contrib.auth.models import auth, User
from django.contrib import messages
from .forms import *

# Create your views here.
def index(request):
    data=Blog.objects.all()
    if request.method=='POST':
        search=request.POST['search']
        result=Blog.objects.filter(heading__contains=search)
        return render(request, 'base.html',{'data':result})
    else:
        return render(request, 'base.html',{'data':data})
    
    
def register(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'you Restration Successfuly created')
            return redirect('/')
    form = RegisterForm()
    return render(request,'register.html',{'form':form}) 


def logIn(request):
    pass
# def register(request):
#     if request.method=='POST':
#         first_name=request.POST['first_name']
#         last_name=request.POST['last_name']
#         username=request.POST['username']
#         email=request.POST['email']
#         password1=request.POST['password1']
#         password2=request.POST['password2']

#         if password1==password2:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request, 'username taken')
#                 return redirect('register')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request, 'email taken')
#                 return redirect('register')
#             else:
#                 user=User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
#                 user.save()
#                 return redirect('login')
#         else:
#             messages.info(request, 'password does not match')
#             return redirect('register')
#     else:
#         return render(request, 'register.html')

# def logIn(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         password=request.POST['password']
#         user=auth.authenticate(username=username, password=password)
#         if user is not None:
#             auth.login(request, user)
#             messages.info(request, 'Logged In Successfully!')
#             return redirect('/')
#         else:
#             messages.info(request, '(Invalid username or password')
#     return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

