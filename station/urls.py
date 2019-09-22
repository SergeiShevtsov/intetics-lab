from django.urls import path
from . import views

urlpatterns= [
    path('station/client_card/', views.new_client, name='new_client'),

    path('station/Order/', views.make_order, name='make_order'),
    path('station/Car/', views.car, name='car'),
    path('Home/orders/', views.orders, name='orders'),
    path('Home/cars/', views.cars, name='cars'),
    path('Home/clients/', views.clients, name='clients'),
    path('station/User/', views.UserF, name='user'),
    path('station/users/', views.userss, name='users'),

]