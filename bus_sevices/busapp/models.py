from django.db import models

# Create your models here.
class busService(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    source=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    time=models.TimeField()
    date=models.DateField()