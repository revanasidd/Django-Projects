from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserBlog(models.Model):
    First_name = models.CharField(max_length=200)
    Last_name =  models.CharField(max_length=200)
    User_name = models.OneToOneField(User,on_delete=models.CASCADE)
    Email = models.EmailField()
    Password = models.CharField(max_length=200)
    Password_conform = models.CharField(max_length=200)

    def __str__(self):
        return self.First_name