from django.urls import path

from . import views

urlpatterns = [
    path("orders/menu/", views.menu, name="menu"),
]
