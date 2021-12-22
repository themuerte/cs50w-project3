from django.urls import path

from .views import menu, order, carrito, delete_order_item, admin

urlpatterns = [
    path("orders/menu/", menu, name="menu"),
    path('order/', order, name="order"),
    path("order/carrito", carrito, name="carrito"),
    path('order/delete_item/<int:pk>', delete_order_item, name="delete_item"),
    path('admin_order/', admin, name="admin_order"),
]
