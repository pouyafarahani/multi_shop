from django.views.generic import ListView

from products.models.product import ProductModel


class ProductListView(ListView):
    model = ProductModel
    template_name = 'products/product_list.html'
    context_object_name = 'products'
