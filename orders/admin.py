from django.contrib import admin

from orders.models import Order, Position


class PositionInline(admin.StackedInline):
    model = Position.orders.through
    extra = 0
    verbose_name = 'Позиция'
    verbose_name_plural = 'Список заказанных товаров'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user', 'created_at', 'product_sum']
    list_display_links = ['__str__']
    inlines = (PositionInline,)
    exclude = ['positions']
    readonly_fields = ['created_at']

    class Meta:
        model = Order
