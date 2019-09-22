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
        return "{} {}, address: {}".format(
            self.first_name, self.last_name, self.date_of_birth, self.address, self.phone, self.email
        )

class Car(models.Model):
    make = models.CharField(max_length=10)
    model = models.CharField(max_length=20)
    year = models.DateField()
    vin = models.CharField(max_length=20)
    client = models.ForeignKey('Client', on_delete=models.PROTECT)
    def __str__(self):
        return "{}: {}, VIN: {}".format(
            self.make, self.model, self.vin
        )

class Order(models.Model):
    date = models.DateField()
    order_Amount = models.IntegerField()

    ORDER_CHOICES = (
        ('Completed', 'Completed'),
        ('In_Progress', 'In Progress'),
        ('Cancelled', 'Cancelled'),
    )
    order_status = models.CharField(max_length=20,choices=ORDER_CHOICES, default='Completed')

    car = models.ForeignKey('Car', on_delete=models.PROTECT)
    def __str__(self):
        return "Date: {}, Order Amount {} $, Order Status: {}".format(
            self.date, self.order_Amount, self.order_status
        )
    
    # car- name of the field
    # Car- name of the class to link

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    secret_word = models.CharField(max_length=20, unique=True, default="")
    def __str__(self):
        return "{} {}, secret word: {}".format(
            self.first_name, self.last_name, self.secret_word
        )





# Create your models here.
