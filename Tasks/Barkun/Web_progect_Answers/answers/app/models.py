from django.db import models
from datetime import datetime


class Question(models.Model):
    question = models.TextField('Задайте вопрос')
    answer = models.TextField('Ответ на вопрос', blank=True)
    issued = models.DateTimeField(default=datetime.now, blank=True)
    author_a = models.CharField('Вы автор ответа! Введите имя или псевдоним', max_length=50, null=True,  blank=True)
    author_q = models.CharField('Вы автор вопроса! Введите имя или псевдоним', max_length=50, null=True,  blank=True)
    def __str__(self) -> str:
        return self.question

    