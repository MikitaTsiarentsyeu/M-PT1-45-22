from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField('Заголовок публикации', max_length=50, blank=False)
    preview = models.CharField('Превью публикации', max_length=500, blank=False) 
    content = models.TextField('Текст публикации', blank=False)
    datetime = models.DateTimeField('Время публикации', default=timezone.localtime)
    image = models.ImageField('Картинка для публикации', upload_to='uploads', blank=True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', blank=True)
    author_name = models.CharField('Имя автора комментария', max_length=50, blank=False)
    comment_text = models.CharField('Текст комментария', max_length=200, blank=False)
    datetime = models.DateTimeField('Время комментария', default=timezone.localtime)
    
    def __str__(self) -> str:
        return self.author_name
    
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
    