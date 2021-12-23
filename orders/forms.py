from django.db import models
from django.forms import ModelForm, fields
from .models import Order, OrderItem, MenuItem

class OrderItemForm(ModelForm):
    class Meta:
        model = OrderItem
        fields = ['amoun','size','extra','extras']
        exclude = ['product', 'order']