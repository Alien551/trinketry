from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def index(request):
    products_list = Product.objects.all()
    context = {'products_list':products_list}
    return render(request, 'shop/index.html', context)

def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {'product':product}
    return render(request, 'shop/product.html', context)
