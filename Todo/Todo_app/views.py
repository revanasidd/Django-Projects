from unicodedata import name
from django.shortcuts import redirect, render
from .forms import TodoForm
from .models import TodoListModel
from django.contrib import messages
# Create your views here.
def home(request):
    data = TodoListModel.objects.all()
    return render(request,'Todo_app/home.html',{'data':data})

def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(f'Your Data Has Been created successfully')
            return redirect('/')
    else:
        form = TodoForm
        return render(request,'Todo_app/createtodo.html',{'form':form})