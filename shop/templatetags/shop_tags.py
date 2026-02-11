from django import template
from django.shortcuts import get_object_or_404
from shop.models import Product

register = template.Library()

@register.simple_tag
def get_all_products_list():
    """Возвращает писок всех товаров."""
    return Product.objects.all()

@register.simple_tag(takes_context=True)
def get_current_product(context):
    """Возращает один продукт по его ключу в таблице"""
    pk = context["pk"]
    return get_object_or_404(Product, pk=pk)
