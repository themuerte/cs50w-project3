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
        ('Su', 'subs'),
        ('Pa', 'pasta'),
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
        verbose_name_plural = "Products"

class OrderItem(models.Model):
    product = models.ForeignKey(MenuItem, models.PROTECT, blank=False, null=False)
    amoun = models.DecimalField(max_digits=20, decimal_places=2, blank=False, null=False)
    extra = models.IntegerField()
    extras = models.TextField(blank=True)

class Order(models.Model):
    state_choices = [ 
        ('AC','Active'),
        ('DE', 'Deactivated')
        ]
    
    menu_item = models.ForeignKey(OrderItem, models.CASCADE, blank=False, null=False)
    user = models.ManyToManyField(User)
    state = models.CharField(max_length=5, choices=state_choices, blank=False)
