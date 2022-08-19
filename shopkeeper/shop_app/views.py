from django.shortcuts import render

from .forms import ProductForm
from .models import Product

# Create your views here.
def index(request):
    return render(request, 'index.html')

def list(request):
    show_data=Product.objects.all()
    return render(request, 'list.html', {'data':show_data})

def form(request):
    if request.method=='GET':
        data_form=ProductForm
    else:
        data_form=ProductForm(request.POST)
        if data_form.is_valid():
            data_form.save()
    return render(request, 'form.html', {'forms':data_form})