from django.db import models

# Create your models here.
class Employee(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    salary=models.DecimalField(max_digits=10, decimal_places=3)
    address=models.TextField()