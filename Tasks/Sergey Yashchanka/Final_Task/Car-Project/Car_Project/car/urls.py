from django.urls import path
from . import views

app_name = 'car'

urlpatterns = [

    path('', views.index, name='car'),
    path('category/<int:cat_id>/', views.category, name='category'),
    path('car/<int:car_id>/', views.car, name='car_id'),
    path('add_car/', views.add_car, name='add_car'),


]
