from django.db import models


class CategoryTransports(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    category = models.ForeignKey(CategoryTransports, on_delete=models.CASCADE)
    image_main = models.ImageField(upload_to='images/')
    image_1 = models.ImageField(upload_to='images/')
    image_2 = models.ImageField(upload_to='images/')
    image_3 = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    text = models.TextField()
    phone = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def __str__(self):
        """Возвращает строковое представление модели."""
        value = len(self.text)
        if value > 50:
            return f"{self.text[:50]}..."
        else:
            return self.text
