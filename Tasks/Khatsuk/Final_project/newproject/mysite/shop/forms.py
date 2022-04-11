from cProfile import label
import django

from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from django.core.exceptions import ValidationError

from .models import Bikes, Category

class BikeModelForm(forms.ModelForm):
    class Meta:
        model = Bikes
        fields = ('title', 'description', 'category', 'brand' ,'year','female', 'teenage',  'children',
        'fork_type',   'fork_material', 'frame_material',
        'frame_suspension','gear_type' ,'front_sprockets',
       'rear_sprockets' ,'wheel_diameter' ,'front_brake_type' ,
        'rear_brake_type' , 'price' ,'in_stock')

class AddBikesModelForm(forms.ModelForm):
    class Meta:
        model = Bikes
        fields = ('title', 'description', 'brand' ,'year','female', 'teenage',  'children',
        'fork_type',   'fork_material', 'frame_material',
        'frame_suspension','gear_type' ,'front_sprockets',
       'rear_sprockets' ,'wheel_diameter' ,'front_brake_type' ,
        'rear_brake_type' , 'price' ,'in_stock' , 'image', 'category')

class SearchdBikesForm(forms.Form):

    title = forms.CharField(required=False, max_length=50, label='модель')
    brand = forms.CharField(required=False,initial='noname', max_length=15, label='производитель')
    year = forms.IntegerField(min_value=2020 , max_value=2025 ,initial=2021, label='год')
    female = forms.BooleanField(required=False, initial=False, label='женский')
    teenage = forms.BooleanField(required=False,initial=False, label='подрастковый')
    children = forms.BooleanField(required=False,initial=False, label='детский')
    fork_type = forms.MultipleChoiceField(initial='a', choices=Bikes.FORK_TYPES, label='тип вилки', widget=CheckboxSelectMultiple)
    fork_material = forms.MultipleChoiceField(initial='a',  choices=Bikes.MATERIALS, label='материал вилки', widget=CheckboxSelectMultiple)
    frame_material = forms.MultipleChoiceField(initial='a',  choices=Bikes.MATERIALS, label='материал рамы', widget=CheckboxSelectMultiple)
    frame_suspension = forms.BooleanField(required=False,initial=False, label='задний амортизатор')
    gear_type = forms.MultipleChoiceField(initial='o', choices=Bikes.GEAR_TYPES, label='тип трансмиссии', widget=CheckboxSelectMultiple)
    front_sprockets = forms.MultipleChoiceField(initial=1, choices=Bikes.FRONT_GEAR,
                                        label='звезд спереди', widget=CheckboxSelectMultiple)
    rear_sprockets = forms.IntegerField(min_value=1 , max_value=12 ,initial=1, label='звезд сзади')
    wheel_diameter = forms.IntegerField(min_value=5 , max_value=29 ,initial=26, label='диаметр колес')
    front_brake_type = forms.MultipleChoiceField(initial='rv', choices=Bikes.BRAKE_F_TYPES,
                                        label='передний тормоз', widget=CheckboxSelectMultiple)
    rear_brake_type = forms.MultipleChoiceField(initial='rv', choices=Bikes.BRAKE_R_TYPES, label='задний тормоз', widget=CheckboxSelectMultiple)
    price = forms.DecimalField(initial=0, max_digits=6, decimal_places=2, label='цена')
    in_stock = forms.MultipleChoiceField(initial=True, choices=Bikes.STOCK, label='наличие', widget=CheckboxSelectMultiple)

    category = forms.ModelMultipleChoiceField(Category.objects.all(),required=False,label='Тип велосипеда', widget=CheckboxSelectMultiple)


    """
    FORK_TYPES = (('h', 'жесткая'), ('a', 'амортизационная'))
    MATERIALS = (('a', 'алюминий'), ('s', 'сталь'), ('c', 'карбон'))
    GEAR_TYPES = (('o', 'с внешним переключением'), ('i', 'с планетарной передачей'), ('s', 'синглспид'))
    BRAKE_F_TYPES = (('rv', 'ободной: вибрейки'), ('dm', 'дисковые механические'), ('dg', 'дисковые гидравлические'),
                     ('cv', 'ободной клещевой'), ('rg', 'ободные гидравлические'), ('no', 'отсутствует'),
                     ('dr', 'барабанный'))
    BRAKE_R_TYPES = (('rv', 'ободной: вибрейки'), ('dm', 'дисковые механические'), ('dg', 'дисковые гидравлические'),
                     ('co', 'ножной'), ('cv', 'ободной клещевой'), ('rg', 'ободные гидравлические'),
                     ('dr', 'барабанный'))
    FRONT_GEAR = ((1, 'одна'), (2, 'две'), (3, 'три'))
    STOCK = ((True, 'есть в наличии'), (False, 'нет в наличии'))"""


    """
        FIELDS = ('title':'icontains', 'brand':'icontains' ,'year':'','female':'', 'teenage':'',  'children':'',
        'fork_type':'',   'fork_material':'', 'frame_material':'',
        'frame_suspension':'','gear_type':'' ,'front_sprockets':'',
       'rear_sprockets':'' ,'wheel_diameter':'' ,'front_brake_type':'' ,
        'rear_brake_type':'' , 'price' :'lte','in_stock':'',  'category':'')"""

