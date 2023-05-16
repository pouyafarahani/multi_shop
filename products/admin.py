from django.contrib import admin

from .models.product_model import ProductModel
from .models.category import Category


admin.site.register(ProductModel)
admin.site.register(Category)

