from django.urls import path

from apps.products.views.product_list import ProductListView
from apps.products.views.product_detail import ProductDetailView

app_name = 'products'

urlpatterns = [
    path('list/', ProductListView.as_view(), name='product_list'),
    path('<int:product_id>/', ProductDetailView.as_view(), name='product_Detail'),
]