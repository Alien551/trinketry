from django.shortcuts import render
from . import utils

# Create your views here.
def index(request):
    """Страница магазина"""
    context = {"title":"Магазин"}
    return render(request, 'shop/index.html', context)

def product_detail(request, product_slug):
    """Страница товара"""
    context = {
        "title":utils.get_product_detail(product_slug).name,
        'product_slug':product_slug
        }
    return render(request, 'shop/product.html', context)
