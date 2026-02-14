from shop.models import Product

def get_product_detail(product_id):
    return Product.objects.get(id=product_id)

def get_product_from_slug(product_slug):
    return Product.objects.get(slug=product_slug)
