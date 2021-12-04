from django.db import models

# Create your models here.

class Product(models.Model):
    size_choices = [
        ('SM', 'small'),
        ('LG', 'large')
        ]

    category_choices = [
        ('RP', 'regular pizza'),
        ('SP', 'siciliam pizza'),
        ('To', 'tippings'),
        ('Su', 'subs'),
        ('Pa', 'pasta'),
        ('Di', 'dinner platters')
        ]
    
    category = models.CharField(max_length=5, choices=category_choices, blank=False)
    name = models.TextField(max_length=50, blank=False)
    size = models.CharField(max_length=5, choices=size_choices, blank=True)
    price_1 = models.FloatField(blank=False)
    price_2 = models.FloatField(blank=True)

    class Meta:
        verbose_name_plural = "Products"

#class MenuItem(models.Model):
#    pass
