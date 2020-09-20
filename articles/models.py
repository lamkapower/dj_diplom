from django.db import models
from products.models import Product


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(
        verbose_name='Дата публикации', auto_now=True)
    product = models.ManyToManyField(
        Product, verbose_name='Товар', related_name='articles')

    class Meta:
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title
