from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import cache_page

from apps.products.models.product import ProductModel

from django.shortcuts import get_object_or_404, render


@method_decorator(cache_page(600), name='dispatch')  # 600sec == 10 min
class ProductDetailView(View):
    def get(self, request, pk):
        product = get_object_or_404(ProductModel.objects.prefetch_related('comments'), pk=pk)
        comment = product.comments.all()
        products_like = ProductModel.objects.filter(featured_products=True)[:8]
        return render(request, 'products/product_detail.html',
                      {'products': product, 'comments': comment, 'products_like': products_like})
