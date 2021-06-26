from django.db import models
from django.urls import reverse

class Author(models.Model):
    name = models.CharField(max_length=150)

    def get_absolute_url(self):
        return reverse('author', kwargs={'author_id': self.pk})

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    desc  = models.TextField(verbose_name='Текст')
    name = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    views = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('view_post', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачы'

