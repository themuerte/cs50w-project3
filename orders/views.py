from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import *
from django.contrib.auth.forms import AuthenticationForm 
from .models import Product, MenuItem, Order

# Create your views here.

def login(request):
    
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request ,username=username, password=password)
    product = Product.objects.all()

    queryset = {
        'user': user,
        'product': product
    }

    if user is not None: #el user es none, mirar que el username y que lo tengo con el email
        print("esta autenticado")
        return render(request, 'menu/menu.html', queryset)
    else:
        return redirect('index')

def menu(request):
    pass

def order(request):
    pass

#el deslogueo esta en las rutas de users