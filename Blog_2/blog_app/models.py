from django.db import models
from django.contrib.auth.models import auth, User

# Create your models here.
class Blog(models.Model):
    heading=models.CharField(max_length=50)
    image=models.ImageField(upload_to='blog_images')
    desc=models.CharField(max_length=2000)
    name=models.CharField(max_length=20)
    date=models.DateField(auto_now_add=True)
    comment=models.CharField(max_length=100, default=0)