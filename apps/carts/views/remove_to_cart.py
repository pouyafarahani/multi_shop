from django.shortcuts import get_object_or_404, redirect

from .cart_detail import *
from apps.products.models.product import ProductModel


def remove_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(ProductModel, id=product_id)
    cart.remove(product)

    return redirect('cart:cart_detail')
