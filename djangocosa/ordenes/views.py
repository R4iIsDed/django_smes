from django.shortcuts import render, redirect
from menu.models import Usuario, Factura, Direccion, Detalle
from django.contrib.auth.models import User
from django.utils.timezone import datetime 
from carrito.carrito import Cart

# Create your views here.

def start_order(request):
    cart = Cart(request)
    ser = request.user.username
    usuar43 = Usuario.objects.get(correo =  ser)
    if request.method == 'post':
        dirr = request.post.get('direccion')
        fact = Factura.objects.create(usuario =usuar43.id_usuario, direcc = dirr, estatus = "por pagar" )
        fact.save()
        for item in cart:
            product = item['product']
            quantity = int(item['quantity'])
            price = product.price * quantity

            item =  Detalle.objects.create(factu = fact.factura, produto = product, price = price, cantidad = quantity)

        return redirect('ver_usuario')
    return redirect('cart')