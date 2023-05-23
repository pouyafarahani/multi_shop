from .cart_detail import *

from django.shortcuts import get_object_or_404, redirect

from apps.products.models.product import ProductModel


def deduct_to_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(ProductModel, id=product_id)
    print(request.POST)
    form = AddToCartProductForm(request.POST)

    if form.is_valid():
        cleaned_deta = form.cleaned_data
        quantity = cleaned_deta['quantity']
        cart.deduct(product, quantity, replace_quantity=cleaned_deta['inplace'])
        print('valid bod')
    else:
        print('bazm valid nistt')
    return redirect('cart:cart_detail')
