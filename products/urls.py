from django.urls import path

from .views import ProductListView, ProductDetailView

app_name = 'products'

urlpatterns = [
    path('list/', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_Detail'),
]
