from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import *


# Create your views here.

def login(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)

def menu(request):
    pass

def order(request):
    pass

#el deslogueo esta en las rutas de users