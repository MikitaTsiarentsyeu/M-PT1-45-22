from django import forms
from .models import *


class AddOffer(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ('name', 'surname', 'patronymic', 'email', 'resume')
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'patronymic': 'Отчество',
            'email': 'Email',
            'resume': 'Резюме'
        }
