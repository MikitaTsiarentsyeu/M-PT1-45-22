from .models import Information
from django.forms import ModelForm, TextInput, Textarea

class InformationForm(ModelForm):
    class Meta:
        model = Information
        fields = ["title","content","author"]
        widgets ={"title":TextInput(attrs = {'class':"label__inner",'placeholder': "Вести название статьи"}),
                  "content": Textarea(attrs={'class': "label__text",'placeholder': "Ввод текста"}),
                  "author": TextInput(attrs={'class':"label__inner",
                                             'placeholder': 'Введите ваш Email ("Email the address")'}),
        }

