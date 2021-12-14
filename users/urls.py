from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("reg/", views.reg, name="reg"),
    path("logout/",  LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name="logout"), #necesita cmabiarse a la pagina que se redirija - mirar lo del redirect
]