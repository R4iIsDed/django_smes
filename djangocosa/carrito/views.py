from django.shortcuts import render

from .carrito import Cart

# Create your views here.



def add_to_cart(request, product_id):
    cart = Cart(request)

    cart.add(product_id)
    return render(request, 'carrito/menu_cart.html')

def cart(request):
    return render(request, 'carrito/cart.html')
def checkout(request):
    return render(request, 'carrito/checkout.html')