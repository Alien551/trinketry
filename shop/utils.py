from shop.models import Product

def get_product_detail(product_slug):
    return Product.objects.get(slug=product_slug)
