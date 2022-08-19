from django.db import models

# Create your models here.
class Stu_details(models.Model):
    id=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)