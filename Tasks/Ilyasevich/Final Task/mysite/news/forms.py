from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    email = forms.EmailField(label='Введите email адрес', widget=forms.EmailInput(attrs={'class': 'form-control'}))


class CommentForm(forms.Form):
    title = forms.CharField(max_length=250, label='Введите ваше имя', widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(max_length=1000, label='Введите текст отзыва', widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}))
    email = forms.EmailField(label='Введите email адрес', widget=forms.EmailInput(attrs={'class': 'form-control'}))


# class Feedback(forms.ModelForm):
#     class Meta:
#         model = News
#         #fields = '__all__'
#         fields = ['title', 'content', 'is_published']
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
#             }