from .models import Question
from django.forms import ModelForm, TextInput, Textarea

class QuestionForm (ModelForm):
    class Meta:
        model = Question
        fields = ["question", "answer", "author_a", "author_q"]
        widgets = {
            "question": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Задайте вопрос'
            }),
            "author_a": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вы автор ответа. Введите свое имя или псевдоним.'
            }),
            "answer": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите ответ'
            }),
            "author_q": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вы автор вопроса. Введите свое имя или псевдоним'
            }),
        }
