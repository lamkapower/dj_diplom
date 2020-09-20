from django.urls import path

from orders.views import create_order
from products.views import (product_page, product_review, category_page,
                            cart_page)

urlpatterns = [
    path('order/', create_order, name='create_order'),
    path('cart/', cart_page, name='cart_page'),
    path('category/<int:pk>/', category_page, name='category_page'),
    path('<int:pk>/', product_page, name='product_page'),
    path('<int:pk>/feedback/', product_review),
]
