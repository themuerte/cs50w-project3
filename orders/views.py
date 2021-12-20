from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import *
from django.contrib.auth.forms import AuthenticationForm 
from .models import OrderItem, MenuItem, Order

# Create your views here.

def menu(request):
    if request.method == 'GET':
        product = MenuItem.objects.all()
        querset = {
            'product':product
        }
        return render(request, "menu/menu.html", querset)
    
    elif request.method == 'POST':
        pass
    
    print("no es get ni post")

def order(request):
    pass

#el deslogueo esta en las rutas de users