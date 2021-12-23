from django.urls import path

from .views import menu, order, carrito, delete_order_item, admin, OrderItemUpdateView, OrderDeleteView

urlpatterns = [
    path("orders/menu/", menu, name="menu"),
    path('order/', order, name="order"),
    path("order/carrito", carrito, name="carrito"),
    path('order/delete_item/<int:pk>', delete_order_item, name="delete_item"),
    path('admin_order/', admin, name="admin_order"),
    path('order/update_item/<int:pk>', OrderItemUpdateView.as_view(), name="update_item"),
    path('order/delete/<int:pk>', OrderDeleteView.as_view(), name="delete_order"),
    
]
