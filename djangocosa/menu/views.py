from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from .models import Usuario, Producto 
from django.contrib import messages

# Create your views here.


def create (request) :
    comp = request.POST.get('email')
    if Usuario.objects.filter(correo=comp).exists():
        messages.error(request,'Ya esta registrado')
    else:
        usuario = Usuario()

        usuario.Rut = request.POST.get('Rut')
        usuario.name = request.POST.get('name')
        usuario.apellido = request.POST.get('apellido')
        usuario.telefono = request.POST.get('telefono')
        usuario.correo = request.POST.get('email')
        usuario.clave = request.POST.get('password')
        usuario.pregunta_id = request.POST.get('security-question')
        usuario.respuesta = request.POST.get('securityanswer')
        usuario = Usuario(rol_id = '1')
        usuario.save()
        User = User.objects.auth.create_user(username = 'email',
                                            email = 'email',
                                          password = 'password')
        User.save()
        return redirect('login')
    return render(request, 'menu/create.html');
 

def login (request) :
    u = request.POST.get('email')
    c = request.POST.get('password')

    User = authenticate(username = u, password = c)

    if User is not None:
        if User.is_active:
            login(request,User)
            return redirect('index')
        else:
            messages.error(request,'Usuario Inactivo')
    else:
        messages.error(request,'Usuario y/o contraseña incorrecta')

    return render(request, 'menu/login.html');


def index(request) :
    return render (request, 'menu/index.html');

def agregar_producto(request):
    
    form = createform()

    if request.method == "POST":

        form = createform(request.POST)

        if form.is_valid():
            
            producto = Producto()

            producto.nombre_prod = form.cleaned_data['nombre']
            producto.descripcion = form.cleaned_data['descripcion']
            producto.precio = form.cleaned_data['precio']
            producto.imagen = form.cleaned_data['imagen']
            producto.categoria = form.cleaned_data['categoria']
            producto.stock = form.cleaned_data['stock']

            producto.save()
        
        else:
            print("tA MALO")

    return render(request, 'menu/agregar_producto.html');

def banadmin(request):
    return render(request, 'menu/banadmin.html');

def borrarcuenta(request):
    return render(request, 'menu/borrarcuenta.html');

def Cactus(request):
    return render(request, 'menu/Cactus.html');

def Carrito(request):
    return render(request, 'menu/Carrito.html');

def Categorias(request):
    return render(request, 'menu/categorias.html');

def changeforgoh(request):
    return render(request, 'menu/changeforgoh.html');

def chNGE(request):
    return render(request, 'menu/chNGE.html');

def compra_cactus1(request):
    return render(request, 'menu/compra_cactus1.html');

def compra_cactus2(request):
    return render(request, 'menu/compra_cactus2.html');

def compra_cactus3(request):
    return render(request, 'menu/compra_cactus3.html');

def compra_cactus4(request):
    return render(request, 'menu/compra_cactus4.html');

def compra_cactus5(request):
    return render(request, 'menu/compra_cactus5.html');

def compra_cactus6(request):
    return render(request, 'menu/compra_cactus6.html');

def Compra_fertilizante1(request):
    return render(request, 'menu/Compra_fertilizante1.html');

def Compra_fertilizante2(request):
    return render(request, 'menu/Compra_fertilizante2.html');

def Compra_fertilizante3(request):
    return render(request, 'menu/Compra_fertilizante3.html');

def Compra_fertilizante4(request):
    return render(request, 'menu/Compra_fertilizante4.html');

def Compra_fertilizante5(request):
    return render(request, 'menu/Compra_fertilizante5.html');

def Compra_fertilizante6(request):
    return render(request, 'menu/Compra_fertilizante6.html');

def Compra_maceta1(request):
    return render(request, 'menu/Compra_maceta1.html');

def Compra_maceta2(request):
    return render(request, 'menu/Compra_maceta2.html');

def Compra_maceta3(request):
    return render(request, 'menu/Compra_maceta3.html');

def Compra_maceta4(request):
    return render(request, 'menu/Compra_maceta4.html');

def Compra_maceta5(request):
    return render(request, 'menu/Compra_maceta5.html');

def Compra_maceta6(request):
    return render(request, 'menu/Compra_maceta6.html');

def Compra_Pago(request):
    return render(request, 'menu/Compra_Pago.html');

def Compra_pesticida1(request):
    return render(request, 'menu/Compra_pesticida1.html');

def Compra_pesticida2(request):
    return render(request, 'menu/Compra_pesticida2.html');

def Compra_pesticida3(request):
    return render(request, 'menu/Compra_pesticida3.html');

def compra_planta1(request):
    return render(request, 'menu/compra_planta1.html');

def Compra_planta2(request):
    return render(request, 'menu/Compra_planta2.html');

def Compra_planta3(request):
    return render(request, 'menu/Compra_planta3.html');

def Compra_planta4(request):
    return render(request, 'menu/Compra_planta4.html');

def Compra_planta5(request):
    return render(request, 'menu/Compra_planta5.html');

def Compra_planta6(request):
    return render(request, 'menu/Compra_planta6.html');

def Contacto(request):
    return render(request, 'menu/Contacto.html');

def create_html(request):
    return render(request, 'menu/create.html')

def editar_producto(request):
    return render(request, 'menu/editar_producto.html');

def eliminar_producto(request):
    return render(request, 'menu/eliminar_producto.html');

def Fertilizante(request):
    prod = Producto.objects.filter(categoria = 3)
    contexto ={
        "prod":prod
        }
    return render(request, 'menu/Fertilizante.html', contexto);

def Flores(request):
    return render(request, 'menu/Flores.html');

def Maceteros(request):
    return render(request, 'menu/Maceteros.html');

def oferta1(request):
    return render(request, 'menu/oferta1.html');

def oferta2(request):
    return render(request, 'menu/oferta2.html');

def oferta3(request):
    return render(request, 'menu/oferta3.html');

def oferta4(request):
    return render(request, 'menu/oferta4.html');

def oferta5(request):
    return render(request, 'menu/oferta5.html');

def oferta6(request):
    return render(request, 'menu/oferta6.html');

def ofertas(request):
    return render(request, 'menu/ofertas.html');

def Perfil_administrador(request):
    return render(request, 'menu/Perfil_administrador.html');

def Pesticidas(request):
    prod = Producto.objects.filter(categoria = 3)
    contexto ={
        "prod":prod
        }
    return render(request, 'menu/Pesticidas.html');

def profile(request):
    return render(request, 'menu/profile.html');

def Cfertilizante(request, id):
    producto = Producto.objects.get(idProducto = id)
    contexto = {
        "producto":producto
    }
    return render(request, 'menu/Cfertilizante.html', contexto)

