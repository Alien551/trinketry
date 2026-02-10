from shop.models import Product

def get_product_detail(pk):
    return Product.objects.get(pk=pk)
