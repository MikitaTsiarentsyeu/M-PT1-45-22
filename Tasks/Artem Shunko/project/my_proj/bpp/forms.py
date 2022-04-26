from django import forms
from .models import *


class AddClaim(forms.ModelForm):
    class Meta:
        model = Claim
        fields = ('name', 'surname', 'phone', 'email',)
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'phone': 'Телефон',
            'email': 'Email',
        }