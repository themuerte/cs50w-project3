from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth import *
from django.contrib.auth.forms import AuthenticationForm 
from .models import OrderItem, MenuItem, Order
from decimal import *

from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import OrderItemForm

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
                    cant_toppings = len(toppings)
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
                        else:
                            precio = Decimal(menu_item.price_1) + Decimal(int(cant_toppings) * 2)

                        order_item = OrderItem.objects.create(product=menu_item, order=order, amoun=precio, size=size, extra=cant_toppings, extras=toppings)
                        order_item.save()
                        order.total += precio
                        order.save()
                else:
                    #subs
                    subs = request.POST.get("menu_item")
                    menu_item = MenuItem.objects.get(pk=subs)
                    if size == 'Small' and menu_item.name != 'Sausage, Peppers & Onions':
                        precio = Decimal(menu_item.price_1) + Decimal(len(toppings) * 0.5)
                    else:
                        precio = Decimal(menu_item.price_2) + Decimal(len(toppings) * 0.5)
                    
                    order_item = OrderItem.objects.create(product=menu_item, order=order, amoun=precio, size=size, extra=len(toppings), extras=toppings)
                    order_item.save()
                    order.total += precio
                    order.save()
                        
            else:   
                #dinner plats
                dinner_plats = request.POST.get("menu_item")
                menu_item = MenuItem.objects.get(pk=dinner_plats)
                if size == 'Large':
                    precio = Decimal(menu_item.price_2)
                else:
                    precio = Decimal(menu_item.price_1)
                
                order_item = OrderItem.objects.create(product=menu_item, order=order, amoun=precio, size=size)
                order_item.save()
                order.total += precio
                order.save()
        else:
            #los demas platillos(pastas o ensaladas)
            item = request.POST.get("menu_item")
            menu_item = MenuItem.objects.get(pk=item)

            precio = Decimal(menu_item.price_1)
            order_item = OrderItem.objects.create(product=menu_item, order=order, amoun=precio)
            order_item.save()
            order.total += precio
            order.save()
    
    print("no es get ni post, asi que xd")
    return redirect('menu')
    

def order(request):
    if request.method == 'GET':
        queryset = {
            'order': Order.objects.filter(Q(state='AC') & Q(user=request.user)).exists()
        }
        return render(request, 'menu/order.html', queryset)

    elif request.method == 'POST':
        order = Order.objects.create(user=request.user, state='AC', total=0) 
        order.save()
        return redirect("menu")
    
    print("no entro a ninguno")

def carrito(request):
    if request.method == 'GET':
        queryset = {
            'orders':Order.objects.filter(user=request.user).all()
        }
        return render(request, 'menu/carrito.html', queryset)
    
    elif request.method == 'POST':
        order = Order.objects.get(pk=request.POST.get("order"))
        order.state = 'WA'
        order.save()
        return redirect('carrito')

def delete_order_item(request, pk):
    if request.method == 'GET':
        order_item = OrderItem.objects.get(pk=pk)
        order = Order.objects.filter(Q(state='AC') & Q(user=request.user)).first()
        order.total -= order_item.amoun
        order.save()
        order_item.delete()
        return redirect('carrito')
    elif request.method == 'POST':
        pass

def admin(request):
    if request.method == 'GET':
        queryset =  {
            'orders': Order.objects.all()
        }
        return render(request, 'menu/admin.html', queryset)
    elif request.method == 'POST':
        order_user = request.POST.get("order")
        order = Order.objects.get(pk=order_user)
        order.state = 'FI'
        order.save()
        
        return redirect("admin_order")

class OrderItemUpdateView(UpdateView):
    model = OrderItem
    form_class = OrderItemForm
    template_name = "menu/order_item_form.html"
    success_url = reverse_lazy("carrito")

"""     def form_valid(self, form):
        obj = form.save(commit=False)
        
        
        return super().form_valid(form)
 """

class OrderDeleteView(DeleteView):
    model = Order
    template_name = "menu/menu_order_delete.html"
    success_url = reverse_lazy("carrito")
 