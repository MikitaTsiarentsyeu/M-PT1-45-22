from django.db import models

class Advertisement(models.Model):
    image = models.ImageField(upload_to='upload')
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text