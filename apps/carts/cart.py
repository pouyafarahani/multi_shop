from apps.products.models.product import ProductModel
from django.contrib import messages


class Cart:

    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product, quantity=1, replace_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0}
        if replace_quantity:
            self.cart[product_id]['quantity'] = quantity  # replace = True
        else:
            self.cart[product_id]['quantity'] += quantity  # replace = false

            messages.success(self.request, 'add cart success')
        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            messages.warning(self.request, 'remove cart success')
            self.save()

    def deduct(self, product, quantity=1, replace_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0}
        if replace_quantity:
            self.cart[product_id]['quantity'] = quantity  # replace = True
        else:
            self.cart[product_id]['quantity'] -= quantity  # replace = false

        if self.cart[product_id]['quantity'] == 0:
            del self.cart[product_id]
            messages.success(self.request, 'remove cart success')
        else:
            messages.success(self.request, 'deduct cart success')

        self.save()

    def save(self):
        self.session.modified = True

    def __iter__(self):
        product_ids = self.cart.keys()
        products = ProductModel.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product_obj'] = product

        for item in cart.values():
            item['total_price'] = item['product_obj'].price * item['quantity']
            yield item

    def __len__(self):
        return len(self.cart.keys())

    def clear(self):
        del self.session['cart']
        self.save()

    def get_total_price(self):
        product_ids = self.cart.keys()

        return sum(item['quantity'] * item['product_obj'].price for item in self)
