from django.db import models


class Post(models.Model):

    POST_TYPES = [('c', 'copyright'), ('p', 'public licensed')]

    title = models.CharField(max_length=200)
    subtitle =models.CharField(max_length=200, blank=True)
    content = models.TextField()
    issued = models.DateTimeField()
    image = models.ImageField(upload_to='upload', blank=True)
    post_type = models.CharField(choices=POST_TYPES, max_length=1)

    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Author(models.Model):

    name = models.CharField(max_length=200)
    email = models.EmailField(primary_key=True)

    def __str__(self) -> str:
        return self.email
