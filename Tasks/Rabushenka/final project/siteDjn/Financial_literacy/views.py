from django.shortcuts import render, redirect
from .models import Information
from .forms import InformationForm

def index(request):
    return render(request, 'Financial_literacy/start_site.html')

def materials(request):
    information = Information.objects.order_by('-id')
    return render(request, 'Financial_literacy/materials.html', {'information': information })

def information(request):
    error = ""
    if request.method =='POST':
        form = InformationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('materials')
        else:
            error = "Ошибка проверте вводимые значения"

    form = InformationForm()
    list = {'form': form, 'error': error }
    return render(request, 'Financial_literacy/Information.html', list)

def news(request):
    return render(request, 'Financial_literacy/news.html')

def pageNotFound(request): pass
