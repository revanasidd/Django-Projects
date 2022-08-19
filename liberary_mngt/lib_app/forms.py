from attr import field
from .models import *
from django.forms import ModelForm
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        
         
     