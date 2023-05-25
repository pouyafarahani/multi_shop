from django.views.generic import TemplateView
from apps.products.models.product import ProductModel


class HomeView(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = ProductModel.objects.select_related().all()
        return context
