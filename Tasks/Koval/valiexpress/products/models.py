import email
from django.urls import reverse
from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=70)
    description  = models.TextField()
    categories = models.ManyToManyField('Category')
    price = models.FloatField()
    count = models.IntegerField()
    rating = models.FloatField(default=0.0)
    count_of_rate = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='upload', default='upload/noimage.png ')
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_id' : self.pk})

    def get_categories(self):
        return ', '.join([str(category) for category in self.categories.all()])

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id' : self.pk})

class Author(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} {self.surname}'