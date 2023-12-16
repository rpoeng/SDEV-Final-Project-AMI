from store.models import Product
class Cart():
    def __init__(self, request):
        self.session = request.session
        #Get the current session key if it exist
        cart = self.session.get('session_key')
        #if user is new, no session key, creates a new one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        #Make sure carts works on all pages on website
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

    def __len__(self): # calls from context_processors.py to display the cart button on all pages
        return len(self.cart)

    def get_products(self):
        # Retrieve ids from cart
        product_ids = self.cart.keys()
        # Use ids to search for product
        products = Product.objects.filter(id__in=product_ids)

        return products

    def get_quants(self):
        quantities = self.cart
        return quantities


    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        #Get Cart
        shopcart = self.cart
        #update cart dictionary
        shopcart[product_id] = product_qty

        self.session.modified = True

        thing = self.cart
        return thing
