from django.views.generic import ListView

from apps.products.models.product import ProductModel


class ProductListView(ListView):
    queryset = ProductModel.objects.all()
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 6
