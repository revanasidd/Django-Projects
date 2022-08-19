from cgitb import reset
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import BookEvent, Family, Business, Culture, Charity, ContactUs
from django.contrib.auth.decorators import login_required
from .forms import bookForm

# Create your views here.
def Register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['first_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Alreday exist')
                return redirect('register')
            else:
                user=User.objects.create_user(first_name=first_name, last_name=last_name,username=username,email=email,password=password1)
                user.save()
                messages.info(request,'Your account has been created')
        else:
            messages.info(request, 'Password did not match')
    return render(request, 'register.html')

def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.info(request, 'Login Successfull')
            return redirect('/')
    return render(request, 'login.html')

def Logout(request):
    auth.logout(request)
    return redirect('/')

def family(request):
    family_data=Family.objects.all()
    return render(request, 'family.html', {'family':family_data})

def charity(request):
    charity_data=Charity.objects.all()
    return render(request, 'charity.html', {'charity':charity_data})

def business(request):
    business_data=Business.objects.all()
    return render(request, 'business.html', {'business':business_data})

def culture(request):
    culture_data=Culture.objects.all()
    return render(request, 'culture.html', {'culture':culture_data})

def Contact_us(request):
    contact_data=ContactUs.objects.all()
    return render(request, 'contact_us.html', {'contact':contact_data})

def home(request):
    if request.method=='POST':
        name = request.POST['name']
        mobile = request.POST['mobile']
        email = request.POST['email']
        message = request.POST['message']

        if ((name and mobile and email and message)==''):
            messages.info(request, 'Invalid form')
            return redirect('home')
        else:
            user=ContactUs(name=name, mobile=mobile, email=email, message=message)
            user.save()
            messages.info(request, 'Message has been sent')
            return redirect('home')
    else:
        return render(request, 'base.html')

@login_required(login_url='login')
def bookEvent(request):
    book_event=BookEvent.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        mobile_number=request.POST['mobile_number']
        location=request.POST['location']
        email=request.POST['email']
        people=request.POST['people']
        date=request.POST['date']
        event=request.POST['event']
        address=request.POST['address']
        message=request.POST['message']

        if ((mobile_number and email and address)==''):
            messages.info(request, 'Fields must be taken')
            return redirect('book_event')
        else:
            guest=BookEvent(name=name, mobile_number=mobile_number,location=location,email=email,people=people,date=date,event=event,address=address,message=message)
            guest.user=request.user
            guest.name=request.user
            guest.save()
            messages.info(request, 'Booking has been successfully')
            return redirect('/')
    return render(request, 'book_event.html', {'book':book_event})

def About_us(request):
    return render(request, 'about.html')

@login_required(login_url='login')
def user_cart(request):
    cart_data=BookEvent.objects.filter(user=request.user)
    return render(request, 'user_cart.html', {'data':cart_data})

def edit(request, id=0):
    if request.method=='GET':
        if id==0:
            form=bookForm
        else:
            bookevt=BookEvent.objects.get(pk=id)
            form=bookForm(instance=bookevt)
    else:
        if id==0:
            form=bookForm(request.POST)
        else:
            bookevt=BookEvent.objects.get(pk=id)
            form=bookForm(request.POST, instance=bookevt)
        if form.is_valid():
            form.save()
            return redirect('cart')
    return render(request, 'edit.html', {'form':form})

def delete(request, id):
    bookevt=BookEvent.objects.get(pk=id)
    bookevt.delete()
    return redirect('cart')