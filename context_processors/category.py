from apps.products.models.product_category import Category


def category_context(request):
    category = Category.objects.all()
    return {'category': category}
