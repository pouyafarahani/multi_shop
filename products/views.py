from django.views.generic import ListView, DetailView

from .models.product import ProductModel


class ProductListView(ListView):
    model = ProductModel
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = ProductModel
    template_name = 'products/product_detail.html'
    context_object_name = 'products'
