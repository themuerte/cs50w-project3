from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth import *
from django.contrib.auth.forms import AuthenticationForm 
from .models import OrderItem, MenuItem, Order
from decimal import *

# Create your views here.

def menu(request):
    if request.method == 'GET':
        product = MenuItem.objects.all()
        querset = {
            'product':product
        }
        return render(request, "menu/menu.html", querset)
    
    elif request.method == 'POST':

        order = Order.objects.filter(Q(state='AC') & Q(user=request.user)).first()

        if request.POST.get('size') is not None:
            size = request.POST.get('size')
            if request.POST.get('toppings') is not None:
                toppings = request.POST.getlist('toppings')
                category = request.POST.get('category')
                if category == 'RP' or category == 'SP':
                    #pizzas
                    cant_toppings = request.POST.get('cantToppings')
                    menu_item = MenuItem.objects.get(category=category)

                    if size == 'Large':
                        precio = Decimal(menu_item.price_2) + Decimal(int(cant_toppings) * 2)
                        order_item = OrderItem.objects.create(product=menu_item, order=order, amoun=precio, size=size, extra=cant_toppings, extras=toppings)
                        order_item.save()
                        order.total += precio
                        order.save()

                        
                    else:
                        if category == 'RP':
                            precio = Decimal(menu_item.price_1) + Decimal(int(cant_toppings) * 1.25)
                        precio = Decimal(menu_item.price_1) + Decimal(int(cant_toppings) * 2)
                        order_item = OrderItem.objects.create(product=menu_item, order=order, amoun=precio, size=size, extra=cant_toppings, extras=toppings)
                        order_item.save()
                        order.total += precio
                        order.save()

                else:
                    #subs
                    pass
            else:
                #dinner plats
                pass
        else:
            #los demas platillos
            pass
    
    print("no es get ni post, asi que xd")
    return redirect('menu')
    


def order(request):
    if request.method == 'GET':
        queryset = {
            'order': Order.objects.filter(Q(state='AC') & Q(user=request.user)).exists()
        }
        return render(request, 'menu/order.html', queryset)

    elif request.method == 'POST':
        print("metodo post en order")
        order = Order.objects.create(user=request.user, state='AC', total=0) 
        order.save()
        return redirect("menu")
    
    print("no entro a ninguno")

def carrito(request):
    if request.method == 'GET':
        queryset = {
            'orders':Order.objects.filter(user=request.user),
            'order_item': OrderItem.objects.filter(order=request.order)
        }
        return render(request, 'menu/carrito.html', queryset)
    
    elif request.method == 'POST':
        pass

#el deslogueo esta en las rutas de users