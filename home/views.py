from django.views import View
from django.shortcuts import render

from products.models.product_model import ProductModel, Category


class HomeView(View):
    product = ProductModel.objects.all()
    category = Category.objects.all()

    def get(self, request):
        print(self.product.values())
        return render(request, 'home/home.html', {'category': self.category, 'products': self.product})
