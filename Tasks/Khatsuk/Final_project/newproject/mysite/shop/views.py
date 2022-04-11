from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from .models import Bikes, Category

from .forms import AddBikesModelForm, SearchdBikesForm, BikeModelForm

#главная страница - список разделов
def index(request):
    categories = Category.objects.all()
    return render(request, 'shop/first.html', {'cat' : categories})

def by_category(request, category_id):
    bikes = Bikes.objects.filter(category=category_id)
    return render(request, 'shop/by_category.html', {'bikes': bikes})

# функция отображения одного велосипеда с описанием
def bike(request, bike_id):
    bike = Bikes.objects.get(pk=bike_id)
    form = BikeModelForm(instance=bike)
    return render(request, 'shop/bike.html', {'form': form, 'bike': bike})


def add_bike(request):

    if request.method == "POST":
        form = AddBikesModelForm(request.POST, request.FILES)

        if form.is_valid():
            bikes = form.save(commit=False)
            bikes.save()
            form.save_m2m()

            return redirect('index')
    else:
        form = AddBikesModelForm()

    return render(request, 'shop/add_bike.html', {'form':form})

def search_bikes(request):

    if request.method == "POST":
        form = SearchdBikesForm(request.POST)

        if form.is_valid():
            """
            FIELDS = {'title':'__icontains', 'brand':'__icontains', 'year':'', 'female':'', ''
            'teenage':'', 'children':'','fork_type':'__in', 'fork_material':'__in', 'frame_material':'__in',
            'frame_suspension':'__in', 'gear_type':'__in', 'front_sprockets':'__in',
            'rear_sprockets':'', 'wheel_diameter':'', 'front_brake_type':'__in',
            'rear_brake_type':'__in', 'price':'__lte', 'in_stock':'__in', 'category':'__in'}

            for k, v in FIELDS.items():
                print(k,'------->',eval(f'form.cleaned_data["{k}"]'))"""

            bikes = Bikes.objects.filter(Q(title__icontains=form.cleaned_data["title"])&
                                         Q(brand__icontains=form.cleaned_data["brand"])&
                                         Q(year=form.cleaned_data["year"])&Q(female=form.cleaned_data["female"])&
                                         Q(teenage=form.cleaned_data["teenage"])&
                                         Q(children=form.cleaned_data["children"])&
                                         Q(fork_type__in=form.cleaned_data["fork_type"])&
                                         Q(fork_material__in=form.cleaned_data["fork_material"])&
                                         Q(frame_material__in=form.cleaned_data["frame_material"])&
                                         Q(frame_suspension=form.cleaned_data["frame_suspension"])&
                                         Q(gear_type__in=form.cleaned_data["gear_type"])&
                                         Q(front_sprockets__in=form.cleaned_data["front_sprockets"])&
                                         Q(rear_sprockets=form.cleaned_data["rear_sprockets"])&
                                         Q(wheel_diameter=form.cleaned_data["wheel_diameter"])&
                                         Q(front_brake_type__in=form.cleaned_data["front_brake_type"])&
                                         Q(rear_brake_type__in=form.cleaned_data["rear_brake_type"])&
                                         Q(price__lte=form.cleaned_data["price"])&
                                         Q(in_stock__in=form.cleaned_data["in_stock"])&
                                         Q(category__in=form.cleaned_data["category"]))


            return render(request, 'shop/by_category.html', {'bikes': bikes})

    else:
        form = SearchdBikesForm()

    return render(request, 'shop/search_bikes.html', {'form':form})