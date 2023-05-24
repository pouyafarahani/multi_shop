from django.db.models import Q

from apps.products.models.product import ProductModel

from django.views.generic import ListView


class SearchResultsListView(ListView):
    model = ProductModel
    context_object_name = 'product_list'
    template_name = 'products/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return ProductModel.objects.filter(Q(title__icontains=query))
