from django.shortcuts import render, redirect
from django.contrib.auth import *
from django.contrib.auth.models import User
from users.forms import LoginForm, RegisterForm
from django.contrib.auth.forms import AuthenticationForm 


# Create your views here.

#esto es donde carga el login y donde se loguea es en una funcion
def index(request):
    form = AuthenticationForm()
    queryset = {
        'form': form
    }

    return render(request, 'accounts/login.html', queryset)

def logout(request):
    
    if request.method=="POST":
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
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            user.save()
        else:
            print("error!!")
            print(request.POST)

    print("POST method")
    return redirect("index")

