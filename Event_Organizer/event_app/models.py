
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Family(models.Model):
    event_type=models.CharField(max_length=200)
    desc=models.CharField(max_length=1200)
    image=models.ImageField(upload_to='family_images')
    food=models.CharField(max_length=200)
    decoration=models.CharField(max_length=200)
    user=models.ForeignKey(User, on_delete=models.CASCADE, default='')

class Culture(models.Model):
    event_type=models.CharField(max_length=200)
    desc=models.CharField(max_length=1200)
    image=models.ImageField(upload_to='culture_images')
    food=models.CharField(max_length=200)
    decoration=models.CharField(max_length=200)
    user=models.ForeignKey(User, on_delete=models.CASCADE, default='')

class Business(models.Model):
    event_type=models.CharField(max_length=200)
    desc=models.CharField(max_length=1200)
    image=models.ImageField(upload_to='culture_images')
    food=models.CharField(max_length=200)
    publicity=models.CharField(max_length=200)
    user=models.ForeignKey(User, on_delete=models.CASCADE, default='')


class Charity(models.Model):
    event_type=models.CharField(max_length=200)
    desc=models.CharField(max_length=1200)
    image=models.ImageField(upload_to='charity_images')
    food=models.CharField(max_length=200)
    sponser=models.CharField(max_length=200)
    user=models.ForeignKey(User, on_delete=models.CASCADE, default='')

class BookEvent(models.Model):
    name=models.CharField(max_length=200)
    mobile_number=models.IntegerField()
    location=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    people=models.CharField(max_length=50)
    date=models.DateField()
    event=models.CharField(max_length=150)
    food=models.CharField(max_length=150, default='')
    address=models.CharField(max_length=1200)
    message=models.TextField(max_length=1200)
    user=models.ForeignKey(User, on_delete=models.CASCADE, default='')

class ContactUs(models.Model):
    name=models.CharField(max_length=120)
    mobile=models.IntegerField()
    email=models.EmailField()
    message=models.CharField(max_length=1120)

    def __str__(self):
        return self.name