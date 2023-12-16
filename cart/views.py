from django.shortcuts import render, get_object_or_404  #Return product or 404 error message
from .cart import Cart
from store.models import Product
from django.http import JsonResponse



def cart_summary(request):

    cart = Cart(request)
    cart_products = cart.get_products
    quantities = cart.get_quants
    return render(request, "cart_summary.html", {"cart_products":cart_products, "quantities":quantities})


def cart_add(request):
    #get the cart
    cart = Cart(request)
    #test for POST
    if request.POST.get('action') == 'post':
        #retrieve item
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        #Looks up product in data base
        product = get_object_or_404(Product, id=product_id)
        #Save to a Session
        cart.add(product=product, quantity=product_qty)

        #Get cart Quantity
        cart_quantity = cart.__len__()
        #return response
        #response = JsonResponse({'Product Name:': product.name})
        response = JsonResponse({'qty:': cart_quantity})
        return response


def cart_delete(request):
    pass


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.update(product=product_id, quantity=product_qty)

        response = JsonResponse({'qty': product_qty})
        return response
        #return redirect('cart_summary')