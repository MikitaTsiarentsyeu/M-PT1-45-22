from .models import Post, Comment
from django.forms import ClearableFileInput, ModelForm, TextInput, Textarea
from datetime import datetime


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'preview', 'content', 'image']
        widgets = {
                'title' : TextInput(attrs={'class' : 'form-comtrol', 'placeholder' : 'Введите заголовок статьи' }),
                'preview' : TextInput(attrs={'class' : 'form-comtrol', 'placeholder' : 'Введите текст превью' }),
                'content' : Textarea(attrs={'class' : 'form-comtrol', 'placeholder' : 'Введите текст статьи' }),
                'image' : ClearableFileInput(attrs={'class' : 'form-comtrol', 'placeholder' : 'Прикрепите изображение' }),
                }
        model.datetime = datetime.now()
        
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['author_name', 'comment_text']
        widgets = {
                'author_name' : TextInput(attrs={'class' : 'form-comtrol', 'placeholder' : 'Введите свое имя' }),
                'comment_text' : Textarea(attrs={'class' : 'form-comtrol', 'placeholder' : 'Введите текст комментария' }),
                }
        model.datetime = datetime.now()