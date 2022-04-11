from django import forms
from django.core.exceptions import ValidationError
from .models import Post

class AddPost(forms.Form):
    title = forms.CharField(max_length=200)
    subtitle = forms.CharField(max_length=200, label="Subtitle")
    content = forms.CharField(widget=forms.Textarea())
    # post_type = forms.ChoiceField(choices=Post.POST_TYPES, label="Post type")
    image = forms.ImageField()



    def clean_subtitle(self):
        subtitle = self.cleaned_data['subtitle']
        title = self.cleaned_data['title']

        if subtitle == title:
            raise ValidationError("values of title and subtitle should be different")

        return subtitle



class AddPostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image')  
        labels = {'title' : 'Тема',
                'content' : 'Текст сообщения',
                'image':'Фото'}
        widgets = {'title' : forms.TextInput(attrs={'class' : 'form-control'}),
        'content' : forms.Textarea(attrs={'class' : 'form-control'}),
        # 'post_type' : forms.Select(attrs={'class' : 'form-control'}),
        }

    # in the widgets was only 'content' : forms.Textarea(),
        # delete subtitle and post_type from field и widjets

        # 'image' : forms.TextInput(attrs={'class' : 'form-control'})