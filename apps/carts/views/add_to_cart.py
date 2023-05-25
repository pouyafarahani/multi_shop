from django.contrib import messages

from .cart_detail import *

from django.shortcuts import get_object_or_404, redirect

from apps.products.models.product import ProductModel


def add_to_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(ProductModel, id=product_id)
    form = AddToCartProductForm(request.POST)

    if form.is_valid():
        cleaned_deta = form.cleaned_data
        quantity = cleaned_deta['quantity']
        cart.add(product, quantity, replace_quantity=cleaned_deta['inplace'])
    else:
        messages.warning(request, 'Unfortunately, there is a problem')
    return redirect('cart:cart_detail')
