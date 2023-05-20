from django.contrib import admin
from .models.product import ProductModel, Category
from .models.product_image import ProductImage
from .models.product_comment import ProductComment


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]


admin.site.register(Category)
admin.site.register(ProductComment)
