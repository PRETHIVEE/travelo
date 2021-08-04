from django.db import models

# Create your models here.
class Destination():
    id: int
    img: str
    days : str
    location: str
    country: str
    price:int
