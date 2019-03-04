from django.db import models


class Product(models.Model):
    products_name = models.CharField(max_length=255)
    products_price = models.FloatField()
    products_stock = models.IntegerField()
    products_urls= models.CharField(max_length=2055)