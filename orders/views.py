from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
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
    
    print("no es get ni post, asi que xd")


def order(request):
    if request.method == 'GET':
        queryset = {
            'menu_item': Order.objects.filter(Q(state='AC') & Q(user=request.user)).exists()
        }
        return render(request, 'menu/order.html', queryset)

    elif request.method == 'POST':
        order = Order(user=request.user, state='AC')
        order.save()
        return redirect("menu")

#el deslogueo esta en las rutas de users