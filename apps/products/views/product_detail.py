from django.views.generic import DetailView

from apps.products.models.product import ProductModel


class ProductDetailView(DetailView):
    model = ProductModel
    template_name = 'products/product_detail.html'
    context_object_name = 'products'
