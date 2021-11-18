from django.db import models

# Create your models here.

class Category(models.Model):
    kind_choices = [
        ('RP', 'regular pizza'),
        ('SP', 'siciliam pizza'),
        ('To', 'tippings'),
        ('Su', 'subs'),
        ('Pa', 'pasta'),
        ('Di', 'dinner platters')
        ]
    name = models.TextField(max_length=50, blank=False)
    kind = models.CharField(max_length=5, choices=kind_choices, blank=True)

class Product(models.Model):
    size_choices = [
        ('SM', 'small'),
        ('LG', 'large')
        ]
    id_category = models.ForeignKey('Category', blank=False, on_delete=models.CASCADE)
    name = models.TextField(max_length=50, blank=False)
    size = models.CharField(max_length=5, choices=size_choices, blank=True)
    price_1 = models.FloatField(blank=False)
    price_2 = models.FloatField(blank=True)

class MenuItem(models.Model):
    pass
