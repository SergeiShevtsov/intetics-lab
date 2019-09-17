from django.shortcuts import render, redirect
from .models import Client, Car, Order
from .forms import ClientForm




def new_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            Client = form.save()
            Client.save()
            return redirect('client_detail', pk=client.pk)
    else:
        form = ClientForm()
    return render(request, 'station_edit.html', {'form': form})


# Create your views here.
