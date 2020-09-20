from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from products.models import Product, Category
from reviews.models import Review


def product_page(request, pk):
    prod = get_object_or_404(Product, pk=pk)
    prod_rev = Review.objects.filter(product=prod)
    can_write = False if request.user in [r.user for r in prod_rev] else True
    return render(request, 'pages/product.html',
                  {'product': prod, 'can_write': can_write,
                   'product_reviews': prod_rev})


def product_review(request, pk):
    if request.method == 'POST':
        if request.user.is_authenticated:
            r = Review(
                user=request.user, text=request.POST.get('description'),
                product=Product.objects.get(id=pk),
                rating=int(request.POST.get('mark')))
            r.save()
        return redirect('product_page', pk=pk)


def category_page(request, pk):
    cat = get_object_or_404(Category, pk=pk)
    p = Paginator(Product.objects.filter(category=cat), 3)
    page = request.GET.get('page')
    return render(request, 'pages/category.html',
                  {'category': cat,
                   'category_products': p.get_page(page)})


def cart_page(request):
    if request.method == 'GET':
        cart = []
        if request.session.get('cart') is not None:
            for product_id, count in request.session.get('cart').items():
                p = Product.objects.get(id=product_id)
                p.count = count
                cart.append(p)
        return render(request, 'pages/cart.html', {'cart': cart})
    if request.method == 'POST':
        cart = {}
        if request.session.get('cart') is not None:
            cart = request.session['cart']
        if request.POST.get('product_id') is not None:
            p = Product.objects.get(id=request.POST.get('product_id'))
            if cart.get(str(p.id)) is None:
                cart[str(p.id)] = 1
            else:
                cart[str(p.id)] += 1
        request.session['cart'] = cart
        return redirect(request.META.get('HTTP_REFERER'))
