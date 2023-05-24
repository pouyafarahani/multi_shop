from django.http import HttpRequest, HttpResponse

from .cart_detail import *

from django.shortcuts import get_object_or_404, redirect

from apps.products.models.product import ProductModel


def deduct_to_cart_view(request: HttpRequest, product_id: int) -> HttpResponse:
    cart = Cart(request)
    product = get_object_or_404(ProductModel, id=product_id)
    form = AddToCartProductForm(request.POST)

    if form.is_valid():
        cleaned_deta = form.cleaned_data
        quantity = cleaned_deta['quantity']
        cart.deduct(product, quantity, replace_quantity=cleaned_deta['inplace'])
    else:
        pass
    return redirect('cart:cart_detail')
