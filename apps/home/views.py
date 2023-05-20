from django.views import View
from django.shortcuts import render

from apps.products.models.product import ProductModel, Category


class HomeView(View):
    product = ProductModel.objects.all()
    category = Category.objects.all()

    def get(self, request):
        return render(request, 'home/home.html', {'category': self.category, 'products': self.product})
