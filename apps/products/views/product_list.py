from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import ListView

from apps.products.models.product import ProductModel


@method_decorator(cache_page(600), name='dispatch')  # 600sec == 10 min
class ProductListView(ListView):
    queryset = ProductModel.objects.all()
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 6
