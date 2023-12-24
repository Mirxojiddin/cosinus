from django.contrib import admin

from product.models import ProductStatus, Product

# Register your models here.

admin.site.register(ProductStatus)
admin.site.register(Product)
