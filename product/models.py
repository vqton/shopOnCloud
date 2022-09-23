from django.db import models

# Create your models here.


class Product(models.Model):
    SKU = models.CharField(max_length=50, primary_key=True)
    product_name = models.CharField(max_length=50)
    specification = models.CharField(max_length=250)


class Categories(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    categories_name = models.CharField(max_length=100)
