from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='page_qa'),
    path('questions', views.questions, name='page_q'),
    path('answers', views.answers, name='page_a'),
    path('add_ans', views.add_ans, name='add_ans'),
]
