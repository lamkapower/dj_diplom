from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from products.models import Product


class Review(models.Model):
    user = models.ForeignKey(
        User, verbose_name='Пользователь', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(
        verbose_name='Дата публикации', auto_now_add=True)
    product = models.ForeignKey(
        Product, verbose_name='Товар', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name='Рейтинг')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f"Review {self.user.username} -" \
               f" {self.published_at.strftime('%Y-%m-%d')}"

    def stars(self):
        return ''.join('★' for i in range(self.rating))
