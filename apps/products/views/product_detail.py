from django.views import View

from apps.products.models.product import ProductModel

from django.shortcuts import get_object_or_404, render


class ProductDetailView(View):
    def get(self, request, pk):
        product = get_object_or_404(ProductModel.objects.prefetch_related('comments'), pk=pk)
        comment = product.comments.all()
        products_like = ProductModel.objects.filter(featured_products=True)[:8]
        return render(request, 'products/product_detail.html',
                      {'products': product, 'comments': comment, 'products_like': products_like})
