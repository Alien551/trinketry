from django.db import models

# Create your models here.
class Product(models.Model):
    objects = models.Manager()

    name = models.CharField("название", max_length=50,)
    description = models.TextField("описание", null=True, blank=True)
    image = models.ImageField("изображение", upload_to='products/')
    cost = models.FloatField("цена",)
    count = models.IntegerField("количество", default=1)
    date = models.DateField("дата публикации", auto_now=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
