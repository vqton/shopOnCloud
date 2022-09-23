from unicodedata import category
from django.db import models

# Create your models here.


class Category(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    categories_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "categories"


class Product(models.Model):
    SKU = models.CharField(max_length=50, primary_key=True)
    product_name = models.CharField(max_length=50)
    specification = models.CharField(max_length=250)
    product_price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
