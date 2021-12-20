from django.shortcuts import render, redirect
from django.contrib.auth import *
from django.contrib.auth.models import User
from users.forms import LoginForm, RegisterForm
from django.contrib.auth.forms import AuthenticationForm 


# Create your views here.

#esto es donde carga el login y donde se loguea es en una funcion
def index(request):

    if request.method == 'GET':
        form = AuthenticationForm()
        queryset = {
            'form': form
        }
        return render(request, 'accounts/login.html', queryset)

    elif request.method == 'POST':
                
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request ,username=username, password=password)

        queryset = {
            'user': user,
        }

        if user is not None: #el user es none, mirar que el username y que lo tengo con el email
            print("esta autenticado")
            return redirect('menu')
        else:
            return redirect('index')
    

def logout(request):
    if request.method=="POST":
        logout(request)
    
    

def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        queryset = {
            'form': form
        }
        return render(request, 'accounts/register.html', queryset)
    
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            user.save()
    
        return redirect("index")

