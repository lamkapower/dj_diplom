from django.contrib.auth.models import User
from django.db import models
from products.models import Product


class Position(models.Model):
    product = models.ForeignKey(
        Product, verbose_name='Товар', on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(
        verbose_name='Колличество', default=0)

    class Meta:
        verbose_name = 'Позицию заказа'
        verbose_name_plural = 'Позиции заказов'

    def __str__(self):
        return f"{self.product.name} - колличество: {self.quantity}"


class Order(models.Model):
    user = models.ForeignKey(
        User, verbose_name='Пользователь', on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    positions = models.ManyToManyField(
        Position, verbose_name='Заказ', related_name='orders')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.id} Order - User {self.user.username}"

    def product_sum(self):
        return sum(p.quantity for p in self.positions.all())
