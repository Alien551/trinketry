from django.contrib import admin
from .models import Product
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields= {"slug":("name",)}
    list_display = ('slug', 'name', 'price', 'quantity', 'discount', 'date')
    list_editable = ('discount',)
    list_display_links = ('slug', 'name')

    fields=(
        "image",
        "name",
        "slug",
        "description",
        ("price", "discount"),
        "quantity",
        #"date",
        )
