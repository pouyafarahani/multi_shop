from django.urls import path
from .views.cart_detail import cart_detail_view
from .views.add_to_cart import add_to_cart_view
from .views.remove_to_cart import remove_cart_view

app_name = 'cart'

urlpatterns = [

    path('', cart_detail_view, name='cart_detail'),
    path('add/<int:product_id>/', add_to_cart_view, name='cart_add'),
    path('remove/<int:product_id>/', remove_cart_view, name='cart_remove'),

]
