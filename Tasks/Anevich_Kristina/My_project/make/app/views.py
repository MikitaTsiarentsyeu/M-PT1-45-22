from django.shortcuts import render, redirect
from .models import Customer, Comments
from .forms import CustomerForm, CommentsForm
# from django.http import HttpResponseRedirect


def home(request):
    error = ''
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/price')
        else:
            error = 'Data is not correct!'    
    form = CustomerForm()
    dict = {
        'form': form,
        'error': error
    }
    return render(request, 'home.html', dict)


def price(request):
    return render(request, 'price.html')

def comments(request):
    error = '' 
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/flag')
        else:
            error= 'Encorrect data entered!'
    form= CommentsForm()
    dict = {
        'form': form,
        'error': error
    }   
    return render(request, 'recorded.html', dict)

def flag(request):
    text = Comments.objects.order_by('-id')      
    return render(request, 'flag.html', {'name': 'Comments', 'text': text})
