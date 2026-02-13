from django.shortcuts import render, redirect

from shop.utils import get_product_detail
from .utils import get_order, get_order_products

# Create your views here.
def index(request):
    # order = get_order(request)
    # order_products = get_order_products(request)
    # context = {"title":"Корзина", "order":order, "order_products":order_products}
    context= {"title":"Корзина"}
    return render(request, 'cart/index.html', context)

def add_product(request, product_slug):
    product_details = get_product_detail(product_slug)
    order = get_order(request)
    order_products = get_order_products(request)
    product = order_products.filter(product=product_details)
    if product.exists():
        pass
        # products = product.first()
        # products.quantity += 1
        # products.save()
    else:
        order_products.create(order=order, product=product_details, quantity=1)

    return redirect(request.META["HTTP_REFERER"])

def change_product(request, product_id):
    ...

def remove_product(request, product_slug):
    product_details = get_product_detail(product_slug)
    order = get_order(request)
    order_products = get_order_products(request)
    product = order_products.filter(product=product_details)
    product.delete()

    return redirect(request.META["HTTP_REFERER"])
