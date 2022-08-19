from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Book(models.Model):
    id = models.CharField(max_length=200,primary_key=True)
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    numberofcopies = models.CharField(max_length=50)
    def __str__(self):
        return self.title
    
class BookStore(models.Model):
    storename=models.CharField(max_length=50)
    Books=models.OneToOneField(Book,on_delete=models.CASCADE)
    location=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    def __str__(self):
        return self.storename