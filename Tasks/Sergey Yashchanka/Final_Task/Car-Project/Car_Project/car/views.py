from django.shortcuts import render, redirect
from .models import Car, CategoryTransports
from .forms import CarForm


def index(request):
    cat = CategoryTransports.objects.all
    car = Car.objects.all
    context = {
        'cat': cat,
        'car': car,
    }
    return render(request, 'car/index.html', context)


def category(request, cat_id):
    cat = CategoryTransports.objects.all
    cars = Car.objects.filter(category=cat_id)
    context = {
        'cars': cars,
        'cat': cat,
    }
    return render(request, 'car/category_car.html', context)


def car(request, car_id):
    cat = CategoryTransports.objects.all
    alone_car = Car.objects.filter(id=car_id)
    context = {
        'alone_car': alone_car,
        'cat': cat,
    }
    return render(request, 'car/alone_car.html', context)


def add_car(request):
    error = ""
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('car:car')
        else:
            error = "form is incorrect"

    form = CarForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'car/add_car.html', data)
