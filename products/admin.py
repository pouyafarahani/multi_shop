from django.contrib import admin
from .models.product_model import ProductModel, Category
from .models.product_image import ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class CategoryInline(admin.TabularInline):
    model = Category
    extra = 1


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    inlines = [CategoryInline, ProductImageInline]

