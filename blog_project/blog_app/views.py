from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages

from blog_app.models import Blog

# Create your views here.
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
                messages.info(request, 'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                # create user
                user=User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
                user.save()
                messages.info(request, 'username created')
                return redirect('login')
        else:
            messages.info(request, 'Password does not match')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.info(request, 'Successfull Login')
        else:
            messages.info(request, 'Invalid username or password')
        return redirect('/')
    return render(request, 'login.html')

def showBlogs(request):
    data=Blog.objects.all()
    return render(request, 'index.html', {'data':data})

def logout(request):
    auth.logout(request)
    return redirect('/')