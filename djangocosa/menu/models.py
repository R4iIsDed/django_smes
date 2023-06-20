from django.db import models

# Create your models here.

class Region(models.Model):
    id_reg=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre

class Comuna(models.Model):
    id_com=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    region=models.ForeignKey(Region,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombre
    
class Rol(models.Model):
    id_rol=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.nombre
    
class Pregunta(models.Model):
    id_preg=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.nombre
    
class Usuario(models.Model):
    id_usuario=models.AutoField(primary_key=True)
    rut=models.CharField(max_length=12)
    nombres=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=30)
    telefono=models.CharField(max_length=10)
    correo=models.CharField(max_length=50)
    clave=models.CharField(max_length=20)
    rol=models.ForeignKey(Rol,on_delete=models.CASCADE)
    pregunta=models.ForeignKey(Pregunta,on_delete=models.CASCADE, null=True)
    respuesta=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.rut
    
class Direccion(models.Model):
    id_direc=models.AutoField(primary_key=True)
    calle=models.CharField(max_length=30)
    num=models.CharField(max_length=20)
    codigo_po=models.CharField(max_length=30)
    comuna=models.ForeignKey(Comuna,on_delete=models.CASCADE)
    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.codigo_po
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nombre_categoria
    
class Producto(models.Model):
    id_prod = models.AutoField(primary_key=True)
    nombre_prod = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=500)
    precio = models.IntegerField()
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to="productos")
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombre_prod
    
class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True)
    fecha_compra = models.DateField()
    estatus = models.CharField(max_length=200)
    cod_despacho = models.CharField(max_length=40)
    costo_despacho = models.IntegerField()
    comp_despacho = models.CharField(max_length=30)
    total = models.IntegerField()
    direccion = models.ForeignKey(Direccion,on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
