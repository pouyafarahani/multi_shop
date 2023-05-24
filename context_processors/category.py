from apps.products.models.product_category import Category
from django.http import HttpRequest


def category_context(request: HttpRequest) -> dict:
    category = Category.objects.all().prefetch_related('category__images')
    return {'category': category}
