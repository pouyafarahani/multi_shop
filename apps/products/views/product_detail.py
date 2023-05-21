from django.views import View

from apps.products.models.product import ProductModel
from apps.products.models.product_comment import ProductComment

from django.shortcuts import get_object_or_404, render


class ProductDetailView(View):
    def get(self, request, pk):
        product = get_object_or_404(ProductModel, pk=pk)
        comment = ProductComment.objects.all()
        products_like = ProductModel.objects.filter(featured_products=True)
        print('#######', products_like)
        return render(request, 'products/product_detail.html',
                      {'products': product, 'comments': comment, 'products_like': products_like})
