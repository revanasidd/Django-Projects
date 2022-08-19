from django.db import models

# Create your models here.
class Product(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    quantity=models.IntegerField()
    price=models.IntegerField()