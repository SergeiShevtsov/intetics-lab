from django.urls import path
from . import views

urlpatterns= [
    path('station/client_card/', views.new_client, name='new_client'),


]