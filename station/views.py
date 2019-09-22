from django.shortcuts import render, redirect
from .models import Client, Car, Order, User
from .forms import ClientForm, UserFForm, OrderForm, CarForm
from django.http import HttpResponseRedirect

def UserF(request):
    if request.method == "POST":
        form = UserFForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return  HttpResponseRedirect('/station/users/')
    else:
        form = UserFForm()
    return render(request, 'sign_edit.html', {'form': form} )

def userss(request):
    user = User.objects.all()
    return render(request, 'users.html', locals())


def new_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save()
            client.save()
            return redirect('clients')
    else:
        form = ClientForm()
    return render(request, 'station_edit.html', {'form': form})


def make_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            order.save()
            return redirect('orders')
            
    else:
        form = OrderForm()
    return render(request, 'order.html', {'form': form})


def car(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save()
            car.save()
            return redirect('cars')
    else:
        form = CarForm()
    return render(request, 'car.html', {'form': form})


def Home(request):
    return render(request, 'Home.html')

def clients(request):
    client = Client.objects.all()
    return render(request, 'clients.html', locals())

def orders(request):
    orders = Order.objects.all()
    return render(request, 'orders.html', locals())

def cars(request):
    cars = Car.objects.all()
    return render(request, 'cars.html', locals())








# Create your views here.
