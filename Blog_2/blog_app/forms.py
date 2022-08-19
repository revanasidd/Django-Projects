from django.forms import ModelForm
from django.contrib.auth.forms import User

from .models import *

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
    
    