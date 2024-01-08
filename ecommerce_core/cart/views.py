from django.shortcuts import render, get_object_or_404
from .cart import Cart
from ecomapp.models import Product
from django.http import JsonResponse

# Create your views here.

def cart_home(request):
    return render(request, 'cart/cart.html', {} )

def cart_add(request):
    #get the cart
    cart = Cart(request)
    
    #test post req
    if request.POST.get('action') == 'post':
        #get stuff
        product_id = int(request.POST.get('product_id'))
        #look product in the DB
        product_objects = get_object_or_404(Product, id = product_id)

        #save it to session
        cart.add(product = product_objects)

        #get cart quantity
        cart_quantity = cart.__len__()

        
        #return response
        
        #response = JsonResponse({'Product Name: ': product_objects.title})
        
        response = JsonResponse({'quantity: ': cart_quantity})
        return response





def cart_delete(request):
    pass

def cart_update(request):
    pass