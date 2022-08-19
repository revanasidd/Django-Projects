from django import forms
from .models import Student

class student_form(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'