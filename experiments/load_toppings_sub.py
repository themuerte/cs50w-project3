import json
from collections import deque

top = ['Italian','Ham + Cheese','Meatball','Tuna']
category = "To"

cont = 27
product = ""

for pro in top:
    product += str({
        "model": "orders.menuitem", 
        "pk": cont, 
        "fields": 
            {
            "category": "Su",
             "name": pro, 
             "size": "", 
             "price_1": 7.75, 
             "price_2": 9.50
            }
        }, )

    cont += 1

toppings = json.dumps(product)
print(toppings)

#despues lo que se hace es tomar la salida escribirla en un archivo json y se le tiene que dar tratamiento por ejemplo quitar las "" del principio y remplazarr ls ' ' por comilas doles
