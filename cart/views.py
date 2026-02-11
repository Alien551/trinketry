from django.shortcuts import render
from .utils import cartData

# Create your views here.
def index(request):
    data = cartData(request)
    order = data["order"]
    order_products = data["order_products"]

    context = {"title":"Корзина", "order":order, "order_products":order_products}
    return render(request, 'cart/index.html', context)

def update_product(request):
    pass