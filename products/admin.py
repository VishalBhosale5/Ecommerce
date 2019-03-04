from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('products_name','products_price','products_stock')

admin.site.register(Product, ProductAdmin)
# Register your models here.
