from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location="../media/products")

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(storage=fs)
    cost = models.IntegerField()
    count = models.IntegerField(default=1)

    def __str__(self):
        return str(self.name)
