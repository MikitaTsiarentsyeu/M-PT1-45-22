from django.db import models


class Offer(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    resume = models.FileField(upload_to="resumes/%Y/%m/%d")
    time_create = models.DateTimeField()
