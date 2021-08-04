from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.
def home(request):
    dest1 = Destination()
    dest1.days = 3
    dest1.location = 'Trivandrum'
    dest1.country = 'Kerala'
    dest1.price = 3333

    return render(request, 'index.html', {'dest1':dest1})
