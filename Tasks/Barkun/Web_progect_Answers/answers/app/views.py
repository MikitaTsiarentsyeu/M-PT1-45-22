from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Question
from .forms import QuestionForm
from datetime import datetime


def index(request):
    questions = Question.objects.order_by('-id')
    return render(request, 'app/index.html', {'title': 'Вопросы и ответы', 'questions': questions})


def questions(request):
    error = ''
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page_qa')
        else:
            error = 'Форма заполнена неверно'
           
    form = QuestionForm()
    context = {'form': form, 'error' : error}
    return render(request, 'app/questions.html', context)
    

def answers(request):
    questions = Question.objects.order_by('-id')
    return render(request, 'app/answers.html', {'title': 'Дать ответ', 'questions': questions})

def add_ans(request):
    error = ''
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page_qa')
        else:
            error = 'Форма заполнена неверно'
           
    form = QuestionForm()
    context = {'form': form, 'error' : error}
    return render(request, 'app/add_ans.html', context)

# Функция для ответов на неотвеченные вопросы

# def add_ans__(request, id):
#     try:
#         ans = Question.get(id=id)
#         if request.method == "POST":
#             ans.answer = request.POST.get("answer")
#             ans. author_a = request.POST.get("author_a")
#             ans. issued = request.POST.get("issued")
#             ans.save()
#             return HttpResponseRedirect("/")
#         else:
#             return render(request, "add_ans.html", {"answer": ans})
#     except Question.DoesNotExist:
#         return HttpResponseNotFound("<h2>Записи не найдено</h2>")

    

