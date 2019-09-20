from django import forms
from .models import Client, Car, Order, Sign

class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'date_of_birth', 'address', 'phone', 'email',)

class SignForm(forms.ModelForm):

    class Meta:
        model = Sign
        fields = ('first_name', 'last_name',)
    
class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('date', 'order_Amount', 'order_status','car')

class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ('make', 'model', 'year', 'vin', 'client')