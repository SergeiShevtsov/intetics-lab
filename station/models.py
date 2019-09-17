from django.db import models
from django.forms import ModelForm
from django import forms

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.EmailField(max_length=75, unique=True)

    def __str__(self):
        return self.email

class Car(models.Model):
    make = models.CharField(max_length=10)
    model = models.CharField(max_length=20)
    year = models.DateField()
    vin = models.CharField(max_length=20)
    client = models.ForeignKey('Client', on_delete=models.PROTECT)


class Order(models.Model):
    date = models.DateField()
    order_Amount = models.IntegerField()
    order_Status = models.IntegerField(unique=True)
    car = models.ForeignKey('Car', on_delete=models.PROTECT)
    # car- name of the field
    # Car- name of the class to link





# Create your models here.
