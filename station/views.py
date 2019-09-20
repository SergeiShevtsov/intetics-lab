from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, Car, Order, Sign
from .forms import ClientForm, SignForm, OrderForm, CarForm




def new_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save()
            client.save()
            return redirect('client_detail', pk=new_client.pk)
    else:
        form = ClientForm()
    return render(request, 'station_edit.html', {'form': form})

def sign_in(request):
    if request.method == "POST":
        form = SignForm(request.POST)
        if form.is_valid():
            return redirect('client_detail', pk=new_client.pk)
    else:
        form = SignForm()
    return render(request, 'sign_edit.html', {'form': form} )

def client_detail(request, pk):
    # return render(request, 'client_detail', pk=client.pk)
    client = get_object_or_404(Post, pk=pk)
    return render(request, 'station/client_detail.html', {'client': client})

def make_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            Order = form.save()
            Order.save()
            return redirect('order_detail', pk=order.pk)
    else:
        form = OrderForm()
    return render(request, 'order.html', {'form': form})

def car(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save()
            car.save()
            return redirect('car_detail', pk=car.pk)
    else:
        form = CarForm()
    return render(request, 'car.html', {'form': form})

def Home(request):
    return render(request, 'Home.html')

def clients(request):
    client = Client.objects.all()
    return render(request, 'clients.html', locals())








# Create your views here.
