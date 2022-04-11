
from django.urls import path, include

from .views import index, by_category, add_bike, search_bikes, bike

urlpatterns = [
    path('<int:category_id>/',by_category, name='by_category'),
    path('',index, name='index'),
    path('details/<int:bike_id>', bike, name='bike'),
    path('add_bike/', add_bike, name='add_bike'),
    path('search_bikes/', search_bikes, name='search_bikes'),
]



