
from django import forms

from .models import BookEvent

class bookForm(forms.ModelForm):
    class Meta:
        model=BookEvent
        fields=['name','event','people','date','address']