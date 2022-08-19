from django.contrib.auth.models import User, auth
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from lib_app.models import *
from datetime import date
from .forms import *
# Create your views here.
def home(request):
    return render(request, 'home.html')

def showBook(request):
    return render(request, 'show_book.html')

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username has been taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email has been taken')
                return redirect('register')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                user.save()
                messages.info(request, 'Your account has been created')
                return redirect('/')
        else:
            messages.info(request, 'Password did not match')
    return render(request, 'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            messages.info(request, 'Login Success')
            return redirect('/')
        messages.info(request, 'invalid username and password')
    return render(request, 'login.html')

@login_required(login_url='login')
def issueBook(request):
    if request.method=='POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Book has been added') 
        else:
            form = BookForm()
            return render(request, 'issue_book.html',{'form':form})

def show_book(request):
    book=Book.objects.filter(user=request.user)
    return render(request, 'show_book.html', {'book':book})

def logout(request):
    auth.logout(request)
    return redirect('/')

def deleteBook(request, id=0):
    book=Book.objects.get(pk=id)
    book.delete()
    return redirect('books')
