import json
from collections import deque

top = ['Sausage','Mushrooms','Onions','Ham','Canadian Bacon', 'Pineapple', 'Eggplant', 'Tomato & Basil', 'Green Peppers', 'Hamburger', 'Spinach', 'Artichoke', 'Buffalo Chicken', 'Barbecue Chicken', 'Anchovies', 'Black Olives', 'Fresh Garlic', 'Zucchini']
price = 1.25
category = "To"

cont = 2
product = ""

for pro in top:
    product += str({
        "model": "orders.menuitem", 
        "pk": cont, 
        "fields": 
            {
            "category": "To",
             "name": pro, 
             "size": "", 
             "price_1": 1.25, 
             "price_2": ""
            }
        }, )

    cont += 1

toppings = json.dumps(product)
print(toppings)

#despues lo que se hace es tomar la salida escribirla en un archivo json y se le tiene que dar tratamiento por ejemplo quitar las "" del principio y remplazarr ls ' ' por comilas doles
