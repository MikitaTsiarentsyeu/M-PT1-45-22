from django.db import models

class Information(models.Model):
    title = models.CharField(max_length = 500)
    content = models.TextField()
    issued = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to='upload', blank = True)

    author = models.ForeignKey('Author', on_delete = models.CASCADE)

    def __str__(self):
        return self.title

class Author(models.Model):

    name = models.CharField(max_length = 500)
    email = models.EmailField(primary_key = True)

    def __str__(self) -> str:
        return self.email