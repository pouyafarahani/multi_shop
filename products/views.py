from django.views.generic import ListView

from .models.product_model import ProductModel


class ProductListView(ListView):
    model = ProductModel
    template_name = 'products/produt_list.html'
    context_object_name = 'products'
