from shop.models import Product
class Cart:
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = request.session['session_key'] = {}

        self.cart = cart

    def add(self, product, quantity=1):
        product_id = str(product.id)

        if product_id in self.cart:
            self.cart[product_id]['quantity'] += quantity
        else:
            self.cart[product_id] = {'price': str(product.price), 'quantity': quantity}

        self.session.modified = True


    def __len__(self):
        return len(self.cart)
        
    def get_product(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        return products