from django.shortcuts import render, redirect
from .forms import *
from datetime import datetime


def index(request):
    if request.method == 'POST':
        form = AddOffer(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.time_create = datetime.now()
            post.save()
            return redirect('answer')
    else:
        form = AddOffer()
    return render(request, 'bpp/base.html', {'form': form})


def answer(request):
    return render(request, 'bpp/answer.html')
