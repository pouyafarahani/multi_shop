from django.urls import path

from .views import ProductListView

app_name = 'products'

urlpatterns = [
    path('list/', ProductListView.as_view(), name='product_list')
]
