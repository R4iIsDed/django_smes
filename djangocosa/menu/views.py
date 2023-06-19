from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from .models import Usuario, Producto , Pregunta, Categoria
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def create_html (request) :
    pre = Pregunta.objects.all()
    {
        "pre":pre
        }
    comp = request.POST.get('email')
    if request.method == "POST":
        if User.objects.filter(username=comp).exists():
            messages.error(request,'Ya esta registrado')
        else:
            
            user243 = Usuario(rut = (request.POST.get('Rut')), nombres = (request.POST.get('name')),
                         apellidos = (request.POST.get('apellido')), telefono = (request.POST.get('telefono')),
                         correo = (request.POST.get('email')), clave = (request.POST.get('password')),
                         pregunta_id = (request.POST.get('security-question')), respuesta = (request.POST.get('securityanswer')),
                         rol_id = '1')
            user243.save()

            user32 = User.objects.create_user(username = comp,
                                                email = comp,
                                              password = request.POST.get('password'))
            
            user32.save()
            return redirect('login')
    return render(request, 'menu/create.html', 
                    {"pre" : pre});
 

def login2 (request) :
    if request.method == "POST":
        u = request.POST.get('email')
        c = request.POST.get('password')

        User = authenticate(request, username = u, password = c)

        if User is not None:
            if User.is_active:
                login(request, User)
                return redirect('index')
            else:
                messages.error(request,'Usuario Inactivo')
        else:
            messages.error(request,'Usuario y/o contraseña incorrecta')

    return render(request, 'menu/login.html');


def index(request) :
    return render (request, 'menu/index.html');

def agregar_producto(request):
    pre = Categoria.objects.all()
    if request.method == "POST":      
        producto = Producto()
        producto.nombre_prod = request.POST.get('nombre')
        producto.descripcion = request.POST.get('descripcion')
        producto.precio = request.POST.get('precio')
        producto.imagen = request.POST.get('imagen') 
        producto.categoria = request.POST.get ('categoria')
        producto.stock = request.POST.get('stock')
        producto.save()
        messages.success(request, "producto agregado")
    else:
        messages.error(request, "uwu")
    return render(request, 'menu/agregar_producto.html', {
        "pre" : pre
    })

def banadmin(request):
    return render(request, 'menu/banadmin.html');

def borrarcuenta(request):
    if Usuario.objects.filter(correo=User.username).exists():
        user2 = User.objects.get(username = User.username)
        user = Usuario.objects.get(correo = user2.username)
        passs = request.POST.get('password')
        if user.clave == passs and user2.password == passs :
            user2.delete()
            user.delete()
            return redirect('login')
        else:
             messages.ERROR('Su contrasena es incorrecta')
    return render(request, 'menu/borrarcuenta.html');

def Cactus(request):
    prod = Producto.objects.filter(categoria = 3)
    return render(request, 'menu/Cactus.html', 
                  {"prod":prod});

def Carrito(request):
    return render(request, 'menu/Carrito.html');

def Categorias(request):
    return render(request, 'menu/categorias.html');

def changeforgoh(request):
    email = request.POST.get('email')
    pre = Pregunta.objects.all()
    if Usuario.objects.filter(correo=email).exists():
        user = Usuario.objects.get(correo = email)
        user2 = User.objects.get(username = user.correo)
        pregun = request.POST.get('securityquestion')
        if user.pregunta == pregun :
            respues = request.POST.get('securityanswer')
            if user.respuesta == respues :
                new = request.POST.get('newpassword')
                user.clave = new
                user.save()
                user2.password = new
                user2.save()
            else:
                messages.error("la respuesta no es la correcta")
        else:
            messages.error("la pregunta de seguridad elegida no es la correcta")
    else: 
        messages.error("el correo no esta registrado")
    return render(request, 'menu/changeforgoh.html', {'pre' : pre});

def chNGE(request ):
    if Usuario.objects.filter(correo=User.username).exists():
        user2 = User.objects.get(username = User.username)
        user = Usuario.objects.get(correo = user2.username)
        passs = request.POST.get('currentpassword')
        npass = request.POST.get('newpassword')
        if user.clave == passs and user2.password == passs :
            user.clave = passs
            user2.password = passs
            user.save()
            user2.save()
            return redirect('logout')
        else:
            messages.ERROR('Su contrasena es incorrecta')
    return render(request, 'menu/chNGE.html');


def Compra_Pago(request):
    return render(request, 'menu/Compra_Pago.html');


def Contacto(request):
    return render(request, 'menu/Contacto.html');

def editar_producto(request):
    return render(request, 'menu/editar_producto.html');


def editarProducto(request):
    idP = request.POST.get('id')
    nombreP = request.POST.get('nombre')
    descripcionP = request.POST.get('descripcion')
    precioP = request.POST.get('precio')
    stockP = request.POST.get('stock')
    imagenP = request.POST.get('imagen')
    categoriaP = request.POST.get('categoria')
    if Producto.objects.filter(id_prod = idP).exists():

        producto = Producto.objects.get(id_prod = idP)
        producto.nombre_prod = nombreP
        producto.descripcion = descripcionP
        producto.precio = precioP
        producto.stock = stockP
        producto.imagen = imagenP
        registroCategoria = Categoria.objects.filter(id_categoria = categoriaP)
        producto.categoria = registroCategoria

        producto.save()
        messages.success(request,'producto actualizado')
    else:
        messages.error(request, "producto no existente")
    return render(request, 'menu/editar_producto.html');

def eliminar_producto(request):
    producto = Producto.objects.all()
    contexto = {
        "pre":producto
    }
    erase = request.POST.get('prod')
    if Producto.objects.filter(id_prod = erase).exists():

        elimi = Producto.objects.get(id_prod = erase)
        elimi.delete()
    else: 
        print("no se loco")
    return render(request, 'menu/eliminar_producto.html', contexto);

def Fertilizante(request):
    prod = Producto.objects.filter(categoria = 5)
    contexto ={
        "prod":prod
        }
    return render(request, 'menu/Fertilizante.html', contexto);

def Flores(request):
    prod = Producto.objects.filter(categoria = 1)
    return render(request, 'menu/Flores.html', 
                  {"prod":prod});

def Maceteros(request):
    prod = Producto.objects.filter(categoria = 4)
    return render(request, 'menu/Maceteros.html', {"prod":prod});
def ofertas(request):
    return render(request, 'menu/ofertas.html');

def Perfil_administrador(request):
    wea = Usuario.objects.filter(correo = User.username)
    return render(request, 'menu/Perfil_administrador.html', {
        "wea" : wea
    });

def Pesticidas(request):
    prod = Producto.objects.filter(categoria = 2)
    return render(request, 'menu/Pesticidas.html', 
                  {"prod":prod});


@login_required
def ver_usuario(request):
    usuario = Usuario.objects.filter(correo=User.username).first()
    return render(request,
                        'menu/profile.html',
                        {'usuario' : usuario})

def Cfertilizante(request, id):
    producto = Producto.objects.get(id_prod = id)
    contexto = {
        "producto":producto
    }
    return render(request, 'menu/Cfertilizante.html', contexto)

def create_admin (request) :
    pre = Pregunta.objects.all()
    {
        "pre":pre
        }
    comp = request.POST.get('email')
    if request.method == "POST":
        if User.objects.filter(username=comp).exists():
            messages.error(request,'Ya esta registrado')
        else:
            
            user243 = Usuario(rut = (request.POST.get('Rut')), nombres = (request.POST.get('name')),
                         apellidos = (request.POST.get('apellido')), telefono = (request.POST.get('telefono')),
                         correo = (request.POST.get('email')), clave = (request.POST.get('password')),
                         pregunta_id = (request.POST.get('security-question')), respuesta = (request.POST.get('securityanswer')),
                         rol_id = '2')
            user243.save()

            user32 = User.objects.create_user(username = comp,
                                                email = comp,
                                              password = request.POST.get('password'))
            
            user32.save()
            return redirect('login')
    return render(request, 'menu/create.html', 
                    {"pre" : pre});


def logout_view(request):
    logout(request)
    return redirect('login')
