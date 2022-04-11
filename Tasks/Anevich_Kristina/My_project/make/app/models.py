from django.db import models

class Customer(models.Model):
    
    def __str__(self):
        return self.name
    
    def __int__(self):
        return self.phone

    name = models.CharField('Name', max_length=30, blank=True)
    phone = models.IntegerField('Number', blank=True)
    
    class Meta:
        verbose_name = 'Name'
        verbose_name_plural = 'Сontact list'

class Comments(models.Model):
    
    def __str__(self):
        return self.user
    
    user = models.CharField('Name', max_length=30, blank=True)
    text = models.CharField('Number', max_length=200, blank=True)
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Comments'
    