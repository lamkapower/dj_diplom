from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    children = models.ManyToManyField(
        "Category", blank=True, verbose_name='Дочерняя категория',
        related_name='parents')

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категория'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_page', kwargs={'pk': self.id})


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    image = models.ImageField(
        upload_to='products_images', verbose_name='Изображение')
    created_at = models.DateTimeField(
        verbose_name='Дата создания', auto_now=True)
    category = models.ManyToManyField(
        Category, verbose_name='Категория', related_name='products')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_page', kwargs={'pk': self.id})
