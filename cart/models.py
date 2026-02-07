from django.db import models
from django.contrib.auth.models import User
from shop.models import Product

# Create your models here.
class UserCart(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    productid = models.ForeignKey(Product, on_delete=models.CASCADE)
