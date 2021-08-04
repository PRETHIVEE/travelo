from django.db import models

# Create your models here.
class Destination(models.Model):

    img = models.ImageField(upload_to='pics') 
    days = models.IntegerField()
    location = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    price = models.IntegerField()
