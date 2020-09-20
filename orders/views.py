from django.shortcuts import redirect

from products.models import Product
from orders.models import Order, Position


def create_order(request):
    if request.method == 'POST':
        order = Order(user=request.user)
        order.save()
        for item in request.POST:
            if item.startswith('product_'):
                p = Product.objects.get(id=item.split('_')[1])
                ptn = Position(product=p, quantity=int(request.POST.get(item)))
                ptn.save()
                order.positions.add(ptn)
        request.session['cart'] = {}
        return redirect('main')
