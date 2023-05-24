from apps.carts.cart import Cart
from django.http import HttpRequest


def cart_context(request: HttpRequest) -> dict:
    cart = Cart(request)
    return {'cart': cart}
