from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from products.forms import ProductForm

from .models import Product, Category

def index(request):
    products = Product.objects.all()
    paginator = Paginator(products, 6)

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'products/products.html', context)

def category(request, category_id):
    selected_category = Category.objects.get(pk=category_id)
    products = Product.objects.filter(categories=selected_category)
    paginator = Paginator(products, 6)

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {
        'selected_category' : selected_category,
        'page_obj': page_obj,
    }
    return render(request, 'products/category.html', context)

def product(request, product_id): 
    selected_product = Product.objects.get(pk=product_id)
    if request.POST.get('select'):
        rate = request.POST.get('select')
        selected_product.rating = ((selected_product.count_of_rate * selected_product.rating) + int(rate))/(selected_product.count_of_rate + 1)
        selected_product.count_of_rate += 1
        selected_product.save()
    context = {
        'selected_product' : selected_product,
    }
    return render(request, 'products/product.html', context)

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid:
            product = form.save()
            return redirect(product)
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form' : form})