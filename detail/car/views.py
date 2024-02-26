from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def index(request):
    if request.method == 'POST':
        data = request.POST
        car_name = data.get('car_name')
        car_desc = data.get('car_desc')
        image = request.FILES.get("car_image")
        Car.objects.create(car_name=car_name,car_desc=car_desc,car_image=image)
        return redirect('/')

    car = Car.objects.all()
    context = {"data":car}

    return render(request, "index.html", context)

def delete_car(request, id):
    queryset = Car.objects.get(id=id)
    queryset.delete()
    return redirect('/')

def update_car(request, id):
    queryset = Car.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        car_name = data.get('car_name')
        car_desc = data.get('car_desc')
        image = request.FILES.get("car_image")
        queryset.car_name = car_name
        queryset.car_desc = car_desc

        if image:
            queryset.car_image = image
        
        queryset.save()
        return redirect('/')
    context = {"data":queryset}
    return render(request, "update.html", context)

def login_page(request):

    if request.method =='POST':
        user_name = request.POST.get("user_name")
        password  = request.POST.get('password')

        if not User.objects.filter(username = user_name).exists():
            messages.error(request, "Invalid username")
            return redirect('/login/')
        
        user = authenticate(username = user_name, password=password)

        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/')

    return render(request, "login.html")


def logout_page(request):
    logout(request)
    return redirect('/login_page/')

def register(request):

    if request.method =='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_name = request.POST.get("user_name")
        password  = request.POST.get('password')

        user = User.objects.filter(username = user_name)

        if user.exists():
            messages.error(request, "Username already existed")
            return redirect('/register/')
        else:
            user = User.objects.create(first_name=first_name, last_name=last_name, username=user_name)
            user.set_password(password)
            user.save()
            messages.info(request, "Account created successfully")
            request.session['registration_success'] = True  # Flag to indicate successful registration
        
    return render(request, "register.html")