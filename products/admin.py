from django.contrib import admin

from products.models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    # list_display = ['company_name', 'id', 'registration_data', 'edit_date', 'verify']
    # list_display_links = ['company_name']

    # search_fields = ['ogrn']

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
