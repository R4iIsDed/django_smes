from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .carrito import Cart
from menu.models import Usuario, Producto, Direccion, Comuna
from django.contrib.auth.models import User

# Create your views here.



def add_to_cart(request, product_id):
    cart = Cart(request)

    cart.add(product_id)
    return render(request, 'carrito/menu_cart.html')

@login_required
def cart(request):
    return render(request, 'carrito/cart.html')

@login_required
def direccion(request):
    if User is not None:
        ser = request.user.username
        usuar43 = Usuario.objects.get(correo =  ser)
        com =  Comuna.objects.all()
        if request.method == "post" :
            newdirec =  Direccion(calle = request.POST.get('direccion'),
                                  num = request.POST.get('numero'),
                                  codigo_po = request.POST.get('codigo'),
                                  comuna = request.POST.get('comuna'),
                                  usuario = usuar43.id_usuario)
            newdirec.save()
            messages.success(request, "se ha guardado con exito")
        return render(request, 'carrito/direccion.html', { "com" : com  })
    else: 
        return redirect ('login')
    
@login_required
def checkout(request):
    if User is not None:
        ser = request.user.username
        usuar43 = Usuario.objects.get(correo =  ser)
        if  Direccion.objects.filter(usuario = usuar43.id_usuario).exists:
            direc = Direccion.objects.filter(usuario = usuar43.id_usuario)
        else:
            messages.error(request, "no cuenta con direcciones agrege una")
    return render(request, 'carrito/checkout.html', {"direc" : direc})

