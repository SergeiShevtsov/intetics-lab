from django import forms
from .models import Client, Car, Order

class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'date_of_birth', 'address', 'phone', 'email',)