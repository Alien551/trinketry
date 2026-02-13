from django.db import models
from django.contrib.auth.models import User
from shop.models import Product

# Create your models here.
class Order(models.Model):
    objects = models.Manager()

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    session_key = models.CharField("ключ сессии", max_length=32, blank=True, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=30, null=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return str(self.user)

    @property
    def total_price(self):
        total = sum(product.total_price for product in self.orderproducts_set.all())
        return total

    @property
    def total_quantity(self):
        total = sum(product.quantity for product in self.orderproducts_set.all())
        return total

class OrderProducts(models.Model):
    objects = models.Manager()

    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    date_ordered = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    def __str__(self):
        return str(self.order)

    @property
    def total_price(self):
        total= self.product.get_sale_price * self.quantity
        return total
