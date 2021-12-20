from django.urls import path

from .views import menu, order

urlpatterns = [
    path("orders/menu/", menu, name="menu"),
    path('order/', order, name="order"),
]
