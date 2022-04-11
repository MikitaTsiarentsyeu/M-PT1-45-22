from .models import Customer, Comments
from django.forms import ModelForm, TextInput, Textarea
 
    
class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "phone"]
        widgets = {
            "name": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your name',
            }),
            "phone": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your number',
            }),  
        }
                
class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ["user", "text"]
        widgets = {
            "user": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name'
                }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your comment'
                }),
            }
       