from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'shop/index.html')

def product(request, product_id):
    context = {'product_id':product_id}
    return render(request, 'shop/product.html', context)
