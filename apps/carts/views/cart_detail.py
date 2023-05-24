from django.shortcuts import render
from django.views.decorators.cache import cache_page

from ..cart import Cart
from ..forms.cart_form import AddToCartProductForm


@cache_page(600)  # 600sec == 10 min
def cart_detail_view(request):
    cart = Cart(request)

    [item.update({'product_update_quantity_form': AddToCartProductForm(initial={
        'quantity': item['quantity'],
        'inplace': True,
    })}) for item in cart]

    return render(request, 'cart/cart_detail.html', {'cart': cart})

