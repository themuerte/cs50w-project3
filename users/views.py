from django.shortcuts import render, redirect
from django.contrib.auth import *
from django.contrib.auth.models import User
from users.forms import LoginForm, RegisterForm

# Create your views here.

#esto es donde carga el login y donde se loguea es en una funcion
def index(request):
    form = LoginForm()
    queryset = {
        'form': form
    }

    return render(request, 'accounts/login.html', queryset)

def logout(request):
    logout(request)

def register(request):
    form = RegisterForm()
    queryset = {
        'form': form
    }

    return render(request, 'accounts/register.html', queryset)
    

def reg(request):
    if request.method == 'GET':
        print("GET method")
    else:
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print("error!!")
            print(request.POST)

    print("POST method")
    return redirect("index")

