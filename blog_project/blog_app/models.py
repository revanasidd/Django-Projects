from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_heading=models.CharField(max_length=50)
    blog_image=models.ImageField(upload_to='blog_images')
    pub_desc=models.CharField(max_length=1500)
    publisher_name=models.CharField(max_length=50)
    pub_date=models.DateTimeField(auto_now_add=True)