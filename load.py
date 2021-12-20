import json
from typing import Deque


top = ['Canadian', 'Bacon', 'Pineapple', 'Eggplant', 'Tomato & Basil', 'Green Peppers', 'Hamburger', 'Spinach', 'Artichoke', 'Buffalo Chicken', 'Barbecue Chicken', 'Anchovies', 'Black Olives', 'Fresh Garlic', 'Zucchini']
price = 1.25
category = "To"

toppings = Deque[pro]

for pro in top:
    product = {
        'category':'To',
        'name': pro,
        'price_1':1.25
    }
    toppings[pro].append(product)

print(toppings)