from django.db import models
from django.utils import dates

# Create your models here.
class TodoListModel(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    date = models.DateField(auto_created=True, blank=True)