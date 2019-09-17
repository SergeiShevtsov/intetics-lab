from django.urls import path
from . import views

urlpatterns= [
    path('station/client_card/', views.new_client, name='new_client'),
    path('client/<int:pk>/', views.client_detail, name='client_detail'),
    path('station/Signing_in/', views.sign_in, name='sign_in'),
    path('station/Order/', views.make_order, name='make_order'),
    path('station/Car/', views.car, name='car'),

]