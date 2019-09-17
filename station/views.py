from django.shortcuts import render
from .models import Client, Car, Order

def main_page(request):
    return render(request, 'main_page.html', {})

# Create your views here.
