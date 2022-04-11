from .models import Car
from django.forms import ModelForm, TextInput, Textarea


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = [
            'category', 'image_main', 'image_1',
            'image_2', 'image_3', 'title',
            'text', 'phone'
        ]
        widgets = {'title': TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Title'
        }),
            'phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'your number phone'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'description'
            })
        }
