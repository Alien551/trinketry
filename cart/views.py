from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from shop.utils import get_product_detail
from .utils import get_order, get_order_products

# Create your views here.
def index(request):
    # order = get_order(request)
    # order_products = get_order_products(request)
    # context = {"title":"Корзина", "order":order, "order_products":order_products}
    context= {"title":"Корзина"}
    return render(request, 'cart/index.html', context)

def add_product(request):
    product_id = request.POST.get("product_id")

    product_details = get_product_detail(product_id)
    order = get_order(request)
    order_products = get_order_products(request)
    product = order_products.filter(product=product_details)
    if product.exists():
        products = product.first()
        products.quantity += 1
        products.save()
    else:
        order_products.create(order=order, product=product_details, quantity=1)

    # return redirect(request.META["HTTP_REFERER"])
    response_data = {
        "message":"Товар успешно добавлен в корзину"
        }

    return JsonResponse(response_data)

def change_product(request):
    ...

def remove_product(request):
    order_products = get_order_products(request)

    #product_slug version
    # product_details = get_product_from_slug(product_slug)
    # product = order_products.filter(product=product_details)
    #product_id version
    product_id = request.POST.get("product_id")
    product = order_products.get(id=product_id)

    product.delete()
    # return redirect(request.META["HTTP_REFERER"])
    order_html= render_to_string(
        "cart/components/orderproduct.html", {"products":order_products}, request=request
    )
    response_data = {
        "message":"Товар удалён из корзины",
        "order_html":order_html,
        }

    return JsonResponse(response_data)
