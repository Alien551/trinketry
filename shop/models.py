from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    objects = models.Manager()

    image = models.ImageField("изображение", upload_to='products/')
    name = models.CharField("название", max_length=50, unique=True)
    slug = models.SlugField("ссылка", max_length=75, blank=True, null=True, unique=True)
    description = models.TextField("описание", null=True, blank=True)
    price = models.DecimalField("цена", max_digits=11, decimal_places = 2,)
    discount = models.DecimalField("скидка %", max_digits=5, decimal_places = 2, default=0)
    quantity = models.IntegerField("количество", default=1)
    date = models.DateField("дата публикации", auto_now_add=True)

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ("id",)


    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse(viewname="shop:product_detail", kwargs={"product_slug":self.slug})

    def get_sale_price(self):
        if self.discount:
            discount = self.price * self.discount / 100
            return round(self.price - discount, 2)
        return self.price
