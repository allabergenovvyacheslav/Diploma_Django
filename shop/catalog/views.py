from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.


def index(request):
    products = [
        {'name': 'Штучный паркет дуб натур 420х70х15', 'price': 2500},
        {'name': 'Штучный паркет дуб селект 420х70х15', 'price': 3200},
        {'name': 'Штучный паркет дуб рустик 420х70х15', 'price': 1900},
    ]
    return render(request, 'catalog/index.html', {'products': products})
