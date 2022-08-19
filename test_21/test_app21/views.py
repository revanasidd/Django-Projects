from ast import Not
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        # mobile=request.POST['mobile']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return render(request, 'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken')
                return render(request, 'register.html')
            # elif User.objects.filter(mobile=mobile):
            #     messages.info(request, 'Phone number already taken')
            #     return render(request, 'register.html')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                user.save()
                messages.info(request, 'Registeration success')
        else:
            messages.info(request, 'Password did not match')
    return render(request, 'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.info(request, 'Login success')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')