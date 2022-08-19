from django import forms
from .models import busService

class busForm(forms.ModelForm):
    class Meta:
        model=busService
        fields='__all__'