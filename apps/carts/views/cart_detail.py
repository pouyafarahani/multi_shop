from django.shortcuts import render

from ..cart import Cart
from ..forms.cart_form import AddToCartProductForm


def cart_detail_view(request):
    cart = Cart(request)

    [item.update({'product_update_quantity_form': AddToCartProductForm(initial={
        'quantity': item['quantity'],
        'inplace': True,
    })}) for item in cart]

    return render(request, 'cart/cart_detail.html', {'cart': cart})

