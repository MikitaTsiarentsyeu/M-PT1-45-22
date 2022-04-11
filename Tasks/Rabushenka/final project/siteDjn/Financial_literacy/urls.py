from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'home'),
    path('materials/', views.materials, name = 'materials'),
    path('information/', views.information, name = 'information'),
    path('news/', views.news, name = 'news'),
]