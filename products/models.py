from django.db import models
from itertools import count, product
from pydoc import describe
from unicodedata import category
from django.db import models
from django.forms import CharField, ImageField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="category_thumbnails")

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.ImageField(upload_to='images')
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name='images')


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    weight = models.IntegerField()
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="product_thumbnails")
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True, blank=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

