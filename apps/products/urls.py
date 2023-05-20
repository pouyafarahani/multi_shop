from django.urls import path

from apps.products.views.product_list import ProductListView
from apps.products.views.product_detail import ProductDetailView
from apps.products.views.rate_comment import rate_comment

app_name = 'products'

urlpatterns = [
    path('list/', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_Detail'),
    path('<int:pk>/product-comment/', rate_comment, name='product_comment'),
]
