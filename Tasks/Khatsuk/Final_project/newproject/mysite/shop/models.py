from django.db import models

class Bikes(models.Model):

    FORK_TYPES = (('h', 'жесткая'), ('a', 'амортизационная'))
    MATERIALS = (('a', 'алюминий'), ('s', 'сталь'), ('c', 'карбон'))
    GEAR_TYPES = (('o', 'с внешним переключением'), ('i', 'с планетарной передачей'), ('s', 'синглспид'))
    BRAKE_F_TYPES = (('rv','ободной: вибрейки'),('dm','дисковые механические'),('dg','дисковые гидравлические'),
                     ('cv','ободной клещевой'),('rg','ободные гидравлические'),('no','отсутствует'),('dr','барабанный'))
    BRAKE_R_TYPES = (('rv','ободной: вибрейки'),('dm','дисковые механические'),('dg','дисковые гидравлические'),
                     ('co','ножной'),('cv','ободной клещевой'),('rg','ободные гидравлические'),('dr','барабанный'))
    FRONT_GEAR = ((1, 'одна'), (2, 'две'), (3, 'три'))
    STOCK = ((True, 'есть в наличии'), (False, 'нет в наличии'))

    title = models.CharField(max_length=50, verbose_name = 'модель')
    description = models.TextField(null=True, max_length=50,verbose_name = 'описание')
    brand = models.CharField(default='noname',max_length=15, verbose_name = 'производитель', blank=True)
    year = models.PositiveSmallIntegerField(default=2021, verbose_name = 'год', blank=True)
    female = models.BooleanField(default =False,verbose_name = 'женский', blank=True)
    teenage = models.BooleanField(default =False, verbose_name = 'подрастковый', blank=True)
    children = models.BooleanField(default =False, verbose_name = 'детский', blank=True)
    fork_type = models.CharField(default='a',max_length=1, choices=FORK_TYPES, verbose_name = 'тип вилки', blank=True)
    fork_material = models.CharField(default='a',max_length=1, choices=MATERIALS, verbose_name = 'материал вилки', blank=True)
    frame_material = models.CharField(default='a',max_length=1, choices=MATERIALS, verbose_name = 'материал рамы', blank=True)
    frame_suspension = models.BooleanField(default =False,verbose_name = 'задний амортизатор', blank=True)
    gear_type = models.CharField(default='o',max_length=1, choices=GEAR_TYPES, verbose_name = 'тип трансмиссии', blank=True)
    front_sprockets = models.PositiveSmallIntegerField(default=1, choices=FRONT_GEAR, verbose_name = 'звезд спереди', blank=True)
    rear_sprockets = models.PositiveSmallIntegerField(default=1, verbose_name = 'звезд сзади', blank=True)
    wheel_diameter = models.PositiveSmallIntegerField(default=26, verbose_name = 'диаметр колес', blank=True)
    front_brake_type = models.CharField(default='rv',max_length=2, choices=BRAKE_F_TYPES, verbose_name = 'передний тормоз', blank=True)
    rear_brake_type = models.CharField(default='rv',max_length=2, choices=BRAKE_R_TYPES, verbose_name = 'задний тормоз', blank=True)
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2, verbose_name = 'цена', blank=True)
    in_stock = models.BooleanField(default=True, choices=STOCK, verbose_name = 'наличие', blank=True)
    image = models.ImageField(null=True,upload_to='upload', verbose_name='фото')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name = 'тип')
    #добавить мета



class Category(models.Model):
    name =  models.CharField(max_length=50, db_index = True, verbose_name = 'Категория')
    description = models.CharField(null=True,max_length=50, verbose_name='описание')
    image = models.ImageField(null=True,upload_to='upload', verbose_name='фото')
    #добавить описание категории
    #картинку
    def __str__(self):
        return self.name