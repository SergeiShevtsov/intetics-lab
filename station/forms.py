from django import forms
from .models import Client, Car, Order, User

class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'date_of_birth', 'address', 'phone', 'email',)

class UserFForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'secret_word',)
    
class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('date', 'order_Amount', 'order_status','car')

class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ('make', 'model', 'year', 'vin', 'client')