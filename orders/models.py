from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import ModelState

# Create your models here.

class MenuItem(models.Model):
    size_choices = [
        ('SM', 'small'),
        ('LG', 'large')
        ]

    category_choices = [
        ('RP', 'regular pizza'),
        ('SP', 'siciliam pizza'),
        ('To', 'toppings'),
        ('ToS', 'toppingsSubs'),
        ('Su', 'subs'),
        ('Pa', 'pasta'),
        ('Sa', 'salads'),
        ('Di', 'dinner platters')
        ]
    
    category = models.CharField(max_length=5, choices=category_choices, blank=False)
    name = models.TextField(max_length=50, blank=False)
    size = models.CharField(max_length=5, choices=size_choices, blank=True)
    price_1 = models.FloatField(blank=False)
    price_2 = models.FloatField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name + "->" + self.category

    class Meta:
        verbose_name_plural = "MenuItem"


class Order(models.Model):
    state_choices = [ 
        ('AC','Active'),
        ('FI', 'Finished'),
        ('WA', 'Waiting')
        ]
    
    user = models.ForeignKey(User, models.CASCADE, related_name="orders")
    date = models.DateField(auto_now_add=True)
    state = models.CharField(max_length=5, choices=state_choices, blank=False)
    total = models.DecimalField(max_digits=20, decimal_places=2, blank=False, null=False)

    def __str__(self):
        return  str(self.pk) +" -> "+ self.user.username +" -> "+ self.state 

class OrderItem(models.Model):
    product = models.ForeignKey(MenuItem, models.CASCADE, blank=False, null=False, related_name="order_item")
    order = models.ForeignKey(Order, models.CASCADE, blank=True, null=True)
    amoun = models.DecimalField(max_digits=20, decimal_places=2, blank=False, null=False)
    size = models.CharField(max_length=40, blank=True, null=True)
    extra = models.IntegerField(blank=True, null=True)
    extras = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.product.name +" -> "+ str(self.order.pk) +" -> "+ self.order.user.username