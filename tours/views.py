from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.
def home(request):
    dest1 = Destination()
    dest1.img = 'pic4.jpg'
    dest1.days = 3
    dest1.location = 'Trivandrum'
    dest1.country = 'Kerala'
    dest1.price = 3333

    dest2 = Destination()
    dest2.img = 'pic1.jpg'
    dest2.days = 5
    dest2.location = 'banglore'
    dest2.country = 'karnataka'
    dest2.price = 5500

    dest3 = Destination()
    dest3.img = 'pic3.jpg'
    dest3.days = 4
    dest3.location = 'Coorg'
    dest3.country = 'karnataka'
    dest3.price = 9999

    dest4 = Destination()
    dest4.img = 'pic2.jpg'
    dest4.days = 6
    dest4.location = 'banglore'
    dest4.country = 'karnataka'
    dest4.price = 5590

    dests = [dest1, dest2, dest3, dest4]

    return render(request, 'index.html', {'dests':dests})
