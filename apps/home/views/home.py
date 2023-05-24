from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView
from apps.products.models.product import ProductModel


@method_decorator(cache_page(600), name='dispatch')  # 600sec == 10 min
class HomeView(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = ProductModel.objects.select_related().all()
        return context
