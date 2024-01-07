class Cart():
    def __init__(self, request):
        self.session = request.session

        #get current session

        cart = self.session.get('session_key')

        #if user is new so no session key so create one

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        #make sure cart is available on every page
        self.cart = cart
    
    def add(self, product):
        product_id = str(product.id)

        #if product is added already

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.discount_price)}
        self.session.modified = True


    def __len__(self):
        return len(self.cart)