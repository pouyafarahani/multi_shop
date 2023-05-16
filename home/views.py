from django.views import View
from django.shortcuts import render

from products.models.product_model import ProductModel
from products.models.category import Category


class HomeView(View):
    featured_product = ProductModel.objects.filter(active=True)
    category = Category.objects.all()

    def get(self, request):
        return render(request, 'home/home.html', {'category': self.category, 'products': self.featured_product})
