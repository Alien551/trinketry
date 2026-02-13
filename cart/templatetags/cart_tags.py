from django import template
from cart.utils import get_order, get_order_products

register = template.Library()

@register.simple_tag()
def order(request):
    return get_order(request)

@register.simple_tag()
def order_products(request):
    return get_order_products(request)
